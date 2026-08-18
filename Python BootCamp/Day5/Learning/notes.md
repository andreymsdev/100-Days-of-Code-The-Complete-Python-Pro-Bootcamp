Para criar senhas fortes em Python, usamos a função `random.choices` junto com um loop `for` ou a função `range` para juntar letras, números e símbolos de forma rápida e segura.

## O que é e como usar o `range`

O `range` cria uma sequência de números inteiros. Usamos ele no comando for para repetir uma ação várias vezes.

- `range(5)` cria uma contagem de 0 até 4 (cinco voltas).
- Você pode definir o início, o fim e o passo: range(inicio, fim, passo).

**Exemplo simples de `range`**

```python
for numero in range(3):
    print(numero)  # Mostra: 0, 1, 2

```

## CONTAGEM REGRESSIVA

```python
# O range para um número antes do final, então usamos -1 para incluir o 0
for i in range(1, -1, -1):
    print(i)

```
