# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Flamengo', 'Atlético Paranaense', 'Fluminense', 'Bahia',
         'Cruzeiro', 'Coritiba', 'Atlético Mineiro', 'Bragantino', 'Corinthias',
         'São Paulo', 'Botafogo', 'Vitória', 'Santos', 'Grêmio',
         'Mirassol', 'Vasco', 'Internacional', 'Remo', 'Chapecoense')

print('-=-'*12)
print(f'Lista de times do Brasileirão 2026: {times}')
print('-=-'*12)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-'*12)
print(f'Os 4 últimos colocados: {times[16:20]}')
print('-=-'*12)
print(f'Em ordem alfabética: {sorted(times)}')
print('-=-'*12)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}ª posição.')
