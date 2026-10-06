# Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também 
# o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
func = {}


func['nome'] = str(input('Nome do funcionário: '))
idade = int(input('Ano de nascimento: '))
func['idade'] = datetime.now().year - idade

ctf = int(input('Carteira de trabalho (0 não tem): '))
func['ctps'] = ctf
if ctf != 0:
    func['contratação'] = int(input('Ano da contratação: '))
    func['salário'] = float(input('Salário: '))
    func['aposentadoria'] = func['idade'] + ((func['contratação'] + 35) - datetime.now().year)

print('-='*20)
for x, y in func.items():
    print(f'— {x} tem o valor {y}')