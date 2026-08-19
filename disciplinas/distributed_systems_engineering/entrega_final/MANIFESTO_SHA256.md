# Manifesto SHA-256 do pacote final

Data da consolidação: 1º de agosto de 2026

Os hashes abaixo identificam os 15 arquivos que compõem o pacote
final: os 14 DOCX institucionais preenchidos e o relatório automatizado de
validação. Os 17 decks HTML e o `index.html` de navegação acompanham o pacote e
não entram no manifesto, por serem regenerados a partir das fontes do
repositório. Para conferir os hashes a partir da raiz do repositório, execute:

```bash
sed -n '/^```text$/,/^```$/p' entrega_final/MANIFESTO_SHA256.md \
  | sed '1d;$d' | sha256sum --check --strict
```

```text
f6e3e734e4faa27b5081c03bbe383f17103b1e1eabb351d1519fcb4953ba2698  entrega_final/Instrumentos Avaliativos/Avaliação final_(10 discursivas)_Distributed Systems Engineering.docx
ea5931813980ea4241600781d21c93e59f41f78710d3cc1e37433aa951c53589  entrega_final/Instrumentos Avaliativos/TEMPLATE ENTREGA DE TRABALHO - Distributed Systems Engineering.docx
0de0e1c67d0877834817eb2fa059acf46596031376c260ce0d532bb9c3f0bcf1  entrega_final/Unidade 1/40 Questões - UNI1_Distributed Systems Engineering.docx
8a7c381214dbbbe9e03b33e7794c3420b28a7682c9b0e14a61a523d6113137cc  entrega_final/Unidade 1/TEMPLATE - Unidade 1_Distributed Systems Engineering.docx
5b37b6ba6747b3965bef99bfbbfdf93160291a897a74141fe114f9b2186a9e6e  entrega_final/Unidade 1/Videoaula_ Introdutória + 1 a 4/Videoaulas Introdutória + 1 a 4 - Validação - Distributed Systems Engineering.docx
412838226680e7f44f5547dadf8c99b534de0eb0d3fe0159a844f452ef372906  entrega_final/Unidade 2/40 Questões - UNI2_Distributed Systems Engineering.docx
bcd4b17e8eb665c9f42804ce0afbca77bf6f22095204fac7ccce45ba444721c2  entrega_final/Unidade 2/TEMPLATE - Unidade 2_Distributed Systems Engineering.docx
e0407fa8f3178eef23698f8fdc95b15365009bdb8e4673f9c24fc4186158ffb5  entrega_final/Unidade 2/Videoaulas 5 a 8/Videoaulas 5 a 8 - Validação - Distributed Systems Engineering.docx
bcd9165c41873db22dea460b7aeea14c78216f847fbf85e5668f728437f198fb  entrega_final/Unidade 3/40 Questões - UNI3_Distributed Systems Engineering.docx
1690513148530574b728f8aa5ee84d6bb382b9ec5f2b7e8fa4c67422e1df7449  entrega_final/Unidade 3/TEMPLATE - Unidade 3_Distributed Systems Engineering.docx
a43c73b21e30cd13400014196b022d18ed0419e5d8d0a53b6771e0aa6a8c6a3f  entrega_final/Unidade 3/Videoaula 9 a 12/Videoaulas 9 a 12 - Validação - Distributed Systems Engineering.docx
2254f2c47351ec8af47e9004270cf3c5182d31ec7fbbc09d6b91dd735b06c324  entrega_final/Unidade 4/40 Questões - UNI4_Distributed Systems Engineering.docx
ae76d49329908112681aefa2d2ec5d19b508cc8f4b6b191e8f29f65bc4f814d1  entrega_final/Unidade 4/TEMPLATE - Unidade 4_Distributed Systems Engineering.docx
c25110d25d144cb7e93a59a440f1e0287baf39cda913ee809ddef010e7db1806  entrega_final/Unidade 4/Videoaula 13 a 16/Videoaulas 13 a 16 - Validação - Distributed Systems Engineering.docx
60c06b093953a5104ba430775064bdfdd02ac0c57e6654600303d7b268a754e9  entrega_final/validacao_docx.json
```
