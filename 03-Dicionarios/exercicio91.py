# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint

dados = {'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}

print('Valores sorteados: ')
for k, v in dados.items():
    print(f'{k} tirou {v}')
    sleep(1)

print('-='*30)
print('=== RANKING DOS PLAYERS ===')
res = sorted(dados.items(), key=lambda item: item[1], reverse=True  )

for i, v in enumerate(res):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)