# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from time import sleep

geral = []
jogador = {}
gols = []

while True:
    gols.clear()
    jogador.update({"nome" : str(input('Nome do jogador: ')) })
    cont = int(input(f'Quantas partidas {jogador.get('nome', 'Não encontrado')} jogou?: '))
    for i in range(cont):
        gols.append(int(input(f'Gols na partida {i+1}: ')))
    jogador.update({"gols": gols[:]})
    jogador.update({"total": sum(gols)})
    geral.append(jogador.copy())
    while True:
        flag = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if flag not in 'SN':
            print('ERRO! Escolha apenas S/N!')
        else:
            break
    if flag == 'N':
        break

print('-='*30)
print(f'{'Cod.'} {'Nome':>5} {'Gols':>9} {'Total':>10}')
print('--'*22)
for codigo, nome in enumerate(geral):
    print(f'{codigo} {nome.get("nome"):>8}',end=' ')
    print(f'    {nome.get('gols')}', end=' ')
    print(f'     {nome.get('total')}')
print('--'*22)

while True:
    print('--'*22)
    escolha = int(input('Estatísticas de qual jogador? [999 para]: '))
    if escolha == 999:
        break
    if escolha >= len(geral):
        print('Não existe jogador com esse número!')
    else:
        print(f' -- Levantamento do jogador {jogador.get('nome')}')
        for c, i in enumerate(geral[escolha]['gols']):
            print(f'Na partida {c+1}, fez {i} gols')
                
print()
print('<<< FIM DO PROGRAMA! >>>')