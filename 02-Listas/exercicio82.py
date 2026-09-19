# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os 
# valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

principal = []
pares = []
impares = []
while True:
    entrada = int(input('Digite um valor: '))
    principal.append(entrada)
    flag = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while flag not in 'SN':
        flag = str(input('Escolha um dos dois! [S/N]: ')).upper().strip()
    if flag in 'N':
        break
for i, v in enumerate(principal):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista principal: {principal}')
print(f'A lista de pares: {pares}')
print(f'A lista de ímpares: {impares}')
