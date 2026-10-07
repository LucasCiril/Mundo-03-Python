# Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

geral = []
pss = {}
cont = 0

while True:
    pss['nome'] = str(input('Nome: '))
    pss['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while pss['sexo'] not in 'MF':
        pss['sexo'] = str(input('ERRO! Escolha [M/F]: ')).strip().upper()
    pss['idade'] = int(input('Idade: '))
    geral.append(pss.copy())
    flag = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if flag in 'N':
        break
print('-='*25)
print(f'=>   Foram cadastradas {len(geral)} pessoas')

for value in geral:
    cont += value['idade']
    
total = cont / len(geral)
print(f'=>   A média de idade é de {total:.2f}')
