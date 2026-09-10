# Crie um programa que tenha uma tupla única 
# com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('--'*9)
print('LISTAGEM DE PREÇO')
print('--'*9)

mercado = ('Lápis',1.75,
           'Borracha',2.0,
           'Caderno',10.0,
           'Mochila', 200.00,
           'Notebook', 2730.00)

for itens in range(0,len(mercado)):
    if itens % 2 ==0:
        print(f'{mercado[itens]:.<30}', end='')
    else:
        print(f'R${mercado[itens]:.2f}')
