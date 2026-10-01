# Faça um programa que ajude um jogador da MEGA SENA
# a criar palpites.O programa vai perguntar quantos jogos 
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta

import random
from time import sleep

print('--'*20)
print('ROLETA DA MEGA SENA')
print('--'*20)
entrada = int(input('Quantos jogos você quer gerar? '))
print('-='*5, end=' ')
print(f'< SORTEANDO {entrada} JOGOS! >', end=' ')
print('-='*5)

for i in range(entrada):
    prin = ((random.sample(range(1,60),6)))
    prin.sort()
    print(f'Jogo {i+1} {prin}')
    sleep(1)
    prin.clear()
    
print('-='*5, end=' ')
print('< BOA SORTE! >', end=' ')
print('-='*5)
