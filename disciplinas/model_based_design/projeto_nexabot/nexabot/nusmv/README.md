# NuSMV nesta disciplina

## O que é a verificação canônica

**A verificação formal oficial desta disciplina roda em
`nexabot/modelcheck.py`, o model checker de estados explícitos escrito do
zero em Python (Aula 10).** Ele é o que o estudante lê, executa e modifica.
Este diretório com NuSMV é material de **comparação com a ferramenta de
mercado** — útil para mostrar que a mesma máquina de estados, verificada por
um checker profissional (BDD/SAT por baixo), dá o mesmo resultado — e não é
pré-requisito de nenhuma aula.

## O NuSMV é instalável neste ambiente? Sim, mas não pelo apt

Testamos: `apt-get install nusmv` falha —

```
E: Impossível encontrar o pacote nusmv
```

— porque o NuSMV não é empacotado no repositório Ubuntu/Debian usado aqui.
**Mas o projeto NuSMV distribui um binário Linux 64-bit oficial**
(<https://nusmv.fbk.eu/downloads.html>), e ele roda sem privilégios de root:

```bash
bash nexabot/nusmv/instalar_nusmv.sh      # baixa e instala em ~/.local/opt/nusmv
bash nexabot/nusmv/rodar_verificacao.sh   # verifica supervisor.smv
```

Isso foi de fato testado neste ambiente, do zero, e funcionou.

### A única pegadinha: `libedit.so.0`

O binário oficial do NuSMV 2.7.1 foi ligado (`link`) contra
`libedit.so.0`, uma ABI de `libedit` que distribuições mais novas (Ubuntu
24.04 "noble", usada aqui) não trazem mais — só `libedit.so.2`:

```
./NuSMV: error while loading shared libraries: libedit.so.0: cannot open shared object file
```

A API que o NuSMV usa dessa biblioteca (edição de linha simples do prompt
interativo) é estável entre essas versões, então um **symlink local**
resolve, sem precisar de root e sem recompilar nada:

```bash
ln -s /usr/lib/x86_64-linux-gnu/libedit.so.2 ~/.local/opt/nusmv/fakelib/libedit.so.0
LD_LIBRARY_PATH=~/.local/opt/nusmv/fakelib ~/.local/opt/nusmv/bin/NuSMV --help
```

`instalar_nusmv.sh` já faz esse symlink automaticamente (via `ldconfig -p`)
e `rodar_verificacao.sh` já exporta o `LD_LIBRARY_PATH` correto. Se
`ldconfig` não encontrar `libedit.so.2` no seu sistema, o script avisa e
explica a alternativa (baixar o `.deb` do pacote `libedit2` com `apt-get
download`, sem precisar instalá-lo com privilégios de root, e extrair a
`.so` de dentro dele com `dpkg-deb -x`).

## O modelo: `supervisor.smv`

`supervisor.smv` é a mesma máquina de estados de `nexabot/supervisor.py`
(mesmos 6 estados, mesmas 6 entradas booleanas, mesma prioridade de
transição), com as propriedades REQ-SAFE-001 a 005 escritas tanto em CTL
(`SPEC`) quanto em LTL (`LTLSPEC`). **REQ-SAFE-006 (temporizado) não está
aqui** — um modelo NuSMV sem extensão de tempo real não tem relógio nativo
apropriado para "no máximo 150 ms"; esse requisito é verificado à parte,
exaustivamente, pelo autômato temporizado de `nexabot/timed.py` (Aula 11).

## Resultado obtido (rodado de verdade neste ambiente)

```
-- specification AG !(torque_habilitado & obstaculo)  is true
-- specification AG (emergencia -> (!torque_habilitado & freio_acionado))  is true
-- specification EF estado = MOVENDO  is true
-- specification  G !(torque_habilitado & obstaculo)  is true
-- specification  G (emergencia -> (!torque_habilitado & freio_acionado))  is true
-- specification  G ((estado = FALHA &  X estado != FALHA) -> rearme)  is true
-- specification  G (((((estado = PARADO_OBSTACULO & !obstaculo) & comando_partir) & !emergencia) & !falha_encoder) ->  X estado = MOVENDO)  is true
```

Todas as 7 especificações (as 5 propriedades REQ-SAFE-001/002/004/005 cada
uma em CTL e LTL, mais a checagem CTL de alcançabilidade de REQ-SAFE-003)
deram `true` — o mesmo veredito que `aula_10/01_explora_estados.py` obtém
com o checker Python escrito do zero.
