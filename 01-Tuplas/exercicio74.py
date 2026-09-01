# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também 
# indique o menor e o maior valor que estão na tupla.

import random

i = tuple(random.randint(1,10) for i in range(5))
print('Valores sorteados: ', end='')
for n in i:
    print(f'{n} ', end='')
print(f'\nMaior valor: {max(i)}')
print(f'Menor valor: {min(i)}')
