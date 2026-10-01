# Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

tri = [[], []]

for i in range(7):
    entrada  = int(input(f'Informe o {i+1}º valor: '))
    if entrada % 2 == 0:
        tri[0].append(entrada)
    else:
        tri[1].append(entrada)
tri[0].sort()
tri[1].sort()

print(f'Os valores digitados que são pares: {tri[0]}')
print(f'Os valores digitados que são ímpares: {tri[1]}')
