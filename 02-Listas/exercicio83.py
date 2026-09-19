# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com
# os parênteses abertos e fechados na ordem correta.

lista = []
lista.append(str(input('Digite uma expressão: ')))

for i in lista:
    if i.count('(') == i.count(')'):
        print('A expressão está correta!')
    else:
        print('A expressão está incorreta!')    
