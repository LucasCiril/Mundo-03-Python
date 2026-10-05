# Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

dados = {}

dados['nome'] = str(input('Nome do aluno: '))
dados['média'] = float(input(f'Média de {dados['nome']}: '))

if dados['média'] >= 7:
    dados['situação'] = 'Aprovado'
elif dados['média'] <= 5:
    dados['situação'] = 'Reprovado'
else:
    dados['situação'] = 'Recuperação'

for k, v in dados.items():
    print(f'{k} é igual a {v}')
