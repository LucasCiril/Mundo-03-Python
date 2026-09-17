# Crie um programa onde o usuário possa digitar vários valores numéricos 
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

n = []
flag = ''
while True:
    entry = (int(input('Digite um valor: ')))
    if entry not in n:
        n.append(entry)
    else:
        print('Número duplicado. Não adicionado.')
    flag = str(input('Quer continuar? [S/N] '))
    while flag not in 'SsNn':
        flag = str(input('Escolha S ou N! '))
    if flag in "Nn":
        break
n.sort()
print(f'A lista em ordem crescente: {n}')
