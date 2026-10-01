# Crie um programa que declare uma matriz de dimensão 3×3 
# e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

m0 = [[], [], []]

for i, v in enumerate(m0):
    while len(m0[0]) != 3:
        m0[0].append(int(input(f'Informe um número para a posição [{i},{len(m0[0])}]: ')))
    while len(m0[1]) != 3:
        m0[1].append(int(input(f'Informe um número para a posição [{i+1},{len(m0[1])}]: ')))
    while len(m0[2]) != 3:
        m0[2].append(int(input(f'Informe um número para a posição [{i+2},{len(m0[2])}]: ')))

for q in m0:
    print(q)
