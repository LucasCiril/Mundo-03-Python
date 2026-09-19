# Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                            
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    flag = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while flag not in 'SN':
        flag = str(input('Escolha uma opção válida! [S/N]: ')).upper().strip()
    if flag in 'N':
        break
lista.sort(reverse=True)
print()
print(f'Foram digitados {len(lista) } elementos.')
print(f'Os valores em ordem decrescente: {lista}')
if lista.count(5) == True:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado!')
