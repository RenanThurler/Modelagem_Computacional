# Otimização do Custo de um Tanque Cilíndrico

Trabalho computacional da disciplina de Modelagem Computacional (UERJ/IPRJ), sobre otimização com restrição usando o método do gradiente com derivadas numéricas e função de penalização.

Autores: Felipe Anderson e Renan Thurler

## Como rodar

Instala a única dependência (matplotlib):

```
pip install matplotlib
```

Roda o script principal:

```
python codigo_principal.py
```

Isso vai printar no terminal as dimensões ótimas do tanque (raio, altura) e o custo mínimo encontrado, além de salvar o gráfico de convergência (`convergencia.png`).

Pra ver os testes com diferentes valores dos parâmetros `mu` (penalidade) e `alpha` (tamanho do passo):

```
python testes_de_parametros.py
```

## Arquivos

- `codigo_principal.py` — implementação principal: função de custo, restrição, função de penalização, derivadas numéricas (diferenças finitas) e o método do gradiente.
- `testes_de_parametros.py` — testes de sensibilidade variando `mu` e `alpha`.
- `convergencia.png` — gráfico de exemplo gerado pelo script principal.
