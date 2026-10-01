# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim 
# contendo a média de cada um e permita que o usuário possa mostrar 
# as notas de cada aluno individualmente.

princ = []

while True:
    n0 = str(input('Nome do aluno: '))
    n1= float(input('1ª nota: '))
    n2 = float(input('2ª nota: '))
    med = (n1 + n2) / 2
    princ.append([n0, [n1, n2], med])
    flag = str(input('Quer continuar? [S/N]')).upper().strip()
    if flag not in 'SN':
        flag = str(input('Quer continuar? [S/N]')).upper().strip()
    if flag in 'N':
        break

print(f'{'No.':<4}{'Nome':<10}{'Média':<8}')
print('--'*10)

for i, a in enumerate(princ):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if opc == 999:
        break
    if opc <= len(princ) - 1:
        print(f'Notas de {princ[opc][0]} são: {princ[opc][1]}')
print('<<< VOLTE SEMPRE! >>>')
