# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

agentes = ('chamber', 'cypher', 'deadlock', 
           'killjoy', 'sage', 'veto', 'vyse')

vogal = ''
for nome in agentes:
    print(f'\nA palavra {nome} contém as vogais: ',end='')
    for i in nome:
        if i in 'AaEeIiOoUu':
            print(f'{i}',end=' ')
    