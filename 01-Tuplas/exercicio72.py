# Crie um programa que tenha uma tupla totalmente preenchida 
# com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado 
# (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove', 
           'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Escolha um número entre 0 e 20: '))
    while num not in range(0,21):
        num = int(input('Escolha inválida! Escolha um número entre 0 e 20: '))
    print(f'Você escolheu o número {extenso[num]}')
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont in 'Ss':
        continue
    if cont in 'Nn':
        break
