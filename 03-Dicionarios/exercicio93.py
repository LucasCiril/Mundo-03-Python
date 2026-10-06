# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato.

jogador = {}
gol = []

jogador['nome'] = str(input('Informe o nome do jogador: '))
cont = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for i in range(cont):
    gol.append(int(input(f'Gols na partida {i+1}: ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)

print('-='*20)
print(jogador)
print('-='*20)

for x, y in jogador.items():
    print(f'O campo {x} tem o valor: {y}')

print('-='*20)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas:')

for x, y in enumerate(jogador['gols']):
    print(f'=>   Na partida {x+1}, fez {y} gols')

print(f'Foram um total de {jogador['total']} gols.')