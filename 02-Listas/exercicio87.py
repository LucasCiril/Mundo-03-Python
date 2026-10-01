# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

m0 = [[], [], []]

for i, v in enumerate(m0):
    while len(m0[0]) != 3:
        m0[0].append(int(input(f'Informe um número para a posição [{i},{len(m0[0])}]: ')))
    while len(m0[1]) != 3:
        m0[1].append(int(input(f'Informe um número para a posição [{i+1},{len(m0[1])}]: ')))
    while len(m0[2]) != 3:
        m0[2].append(int(input(f'Informe um número para a posição [{i+2},{len(m0[2])}]: ')))

print('-='*30)
for q in m0:
    print(q)
print('-='*30)

par = []
for q in m0:
    for m in q:
        if m % 2 == 0:
            par.append(m)
soma1 = sum(par)
print(f'A soma dos números pares é {soma1}')

terceira = []
add = 1
for i, v in enumerate(m0):
    terceira.append(v[2])
soma2 = sum(terceira)
print(f'A soma dos números da terceira coluna é {soma2}')

maior = []
for i, v in enumerate(m0[1]):
    maior.append(v)
if maior[0] > maior[1] and maior[0] > maior[2]:
    print(f'O maior número da segunda coluna é {maior[0]}')
elif maior[1] > maior[0] and maior[1]> maior[2]:
    print(f'O maior número da segunda coluna é {maior[1]}')
else:
    print(f'O maior número da segunda coluna é {maior[2]}')
