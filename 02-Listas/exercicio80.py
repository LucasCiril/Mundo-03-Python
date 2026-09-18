# Crie um programa onde o usuário possa digitar cinco valores numéricos 
# e cadastre-os em uma lista, já na posição correta de inserção 
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

l = []

for i in range(0,5):
    nm = int(input('Informe um número: '))
    if i == 0 or nm > l[-1]:
        l.append(nm)
    else:
        pos = 0
        while pos < len(l):
            if nm <= l[pos]:
                l.insert(pos, nm)
                break
            pos += 1
    print(l)
print(f'A lista digitada na ordem: {l}')