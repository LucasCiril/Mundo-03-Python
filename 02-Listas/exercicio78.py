# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado 
# e as suas respectivas posições na lista.

vl = list()
maior = menor = None

for i in range(0,5):
    n = int(input('Informe um número: '))
    vl.append(n)

    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n

print(f'Você digitou os valores {vl}')

print(f'O maior valor digitado foi {maior} nas posições ',end='')
for c, v in enumerate(vl):
    if v == maior:
        print(f'{c}...',end='')
print()

print(f'O menor valor digitado foi {menor} na posição ', end='')
for c, v in enumerate(vl):
    if v == menor:
        print(f'{c}...',end='')
