import os
import re
import time
import hashlib
import json
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "assets"


def load_env(env_path: Path) -> dict:
    env = {}
    if not env_path.exists():
        return env
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' not in line:
            continue
        key, val = line.split('=', 1)
        val = val.strip().strip('"').strip("'")
        env[key.strip()] = val
    return env


def cloudinary_upload(file_path: Path, cloud_name: str, api_key: str, api_secret: str, folder: str | None = None, public_id: str | None = None) -> dict:
    url = f"https://api.cloudinary.com/v1_1/{cloud_name}/image/upload"
    timestamp = int(time.time())
    params = {
        'timestamp': str(timestamp),
    }
    if folder:
        params['folder'] = folder
    if public_id:
        params['public_id'] = public_id
    # Build signature: sort by key, join as key=value, append api_secret
    to_sign = '&'.join(f"{k}={params[k]}" for k in sorted(params.keys())) + api_secret
    signature = hashlib.sha1(to_sign.encode('utf-8')).hexdigest()

    data = {
        'api_key': api_key,
        'timestamp': params['timestamp'],
        'signature': signature,
    }
    if folder:
        data['folder'] = folder
    if public_id:
        data['public_id'] = public_id

    with open(file_path, 'rb') as f:
        files = {'file': (file_path.name, f)}
        resp = requests.post(url, data=data, files=files, timeout=60)
    resp.raise_for_status()
    return resp.json()


def is_image(path: Path) -> bool:
    exts = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'}
    return path.suffix.lower() in exts


def main():
    env = load_env(ROOT / '.env')
    cloud_name = env.get('CLOUDINARY_CLOUD_NAME')
    api_key = env.get('CLOUDINARY_API_KEY')
    api_secret = env.get('CLOUDINARY_API_SECRET')
    if not all([cloud_name, api_key, api_secret]):
        raise SystemExit('CLOUDINARY_* variáveis ausentes no .env')

    folder = 'estrutura_pontes'

    assets = [p for p in ASSETS_DIR.iterdir() if p.is_file() and is_image(p)]
    mapping = {}

    for p in assets:
        public_id = p.stem
        try:
            info = cloudinary_upload(p, cloud_name, api_key, api_secret, folder=folder, public_id=public_id)
            url = info.get('secure_url') or info.get('url')
            if not url:
                raise RuntimeError(f"Upload sem URL para {p}")
            # Map both with and without leading ./
            rel = f"assets/{p.name}"
            mapping[rel] = url
            mapping[f"./{rel}"] = url
            print(f"OK {p.name} -> {url}")
        except Exception as e:
            print(f"FALHA {p}: {e}")

    # Replace in markdown files
    md_files = list(ROOT.glob('*.md'))
    replaced_counts = {}
    if mapping:
        # Pattern to match src="..." referencing assets/
        pattern = re.compile(r'(src=\")(\.\/)?assets\/[^\"]+(\")')
        for md in md_files:
            text = md.read_text()
            original = text

            # Replace using mapping keys to be precise
            for k, v in mapping.items():
                text = text.replace(f'src="{k}"', f'src="{v}"')
                text = text.replace(f"src='{k}'", f"src='{v}'")

            if text != original:
                md.write_text(text)
                replaced = sum(1 for k in mapping.keys() if k in original)
                replaced_counts[md.name] = replaced

    # Save a report for traceability
    (ROOT / 'cloudinary_report.json').write_text(json.dumps({
        'uploaded': mapping,
        'replacements': replaced_counts,
    }, ensure_ascii=False, indent=2))

    print('Concluído.')
    print(json.dumps({'replacements': replaced_counts}, ensure_ascii=False))


if __name__ == '__main__':
    main()

