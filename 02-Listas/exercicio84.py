# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

geral = list()
dado = list()
pesado = leve = None

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    geral.append(dado[:])
    dado.clear()

    flag = str(input('Quer continuar? [S/N]: ')).lower().strip()

    while flag not in 'sn':
        flag = str(input('Quer continuar? [S/N]: ')).lower().strip()

    if flag in 'n':
        break

print(f'Ao todo, foram cadastradas {len(geral)} pessoa(s).')

for nome, peso in geral:
    if pesado is None or peso > pesado:
        pesado = peso

    if leve is None or peso < leve:
        leve = peso

print(f'O maior peso registrado foi {pesado:.2f} kg.')

print(f'O menor peso registrado foi {leve:.2f} kg.')

print('Pessoas mais pesadas: ', end=' ')
for name, peso in geral:
    if peso == pesado:
        print(f'[{name}]',end=' ')

print()

print('Pessoas mais leves: ', end=' ')
for name, peso in geral:
    if peso == leve:
        print(f'[{name}]', end=' ')
