# Desenvolva um programa que leia quatro valores pelo teclado 
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


i = tuple(int(input('Informe um valor: '))for i in range(4))
print(f'Você digitou os números {i}')
print(f'O número 9 ocorreu {i.count(9)} vezes.')
if 3 in i:
    print(f'O valor 3 apareceu a primeira vez na posição {i.index(3)+1}')
else:
    print('O valor 3 não foi informado.')
print(f'Os valores pares digitados foram:', end='')
for even in i:
    if even % 2 == 0:
        print(even, end=' ')
