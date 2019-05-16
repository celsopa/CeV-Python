# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

listaNum = []
for x in range(5):
    num = int(input(f'Digite o {x+1}º número: '))
    if x == 0:
        listaNum.append(num)
        print(f'O número {num} foi adicionado ao final da lista...')
    else:
        for i, v in enumerate(listaNum):
            if num < v:
                listaNum.insert(i, num)
                print(f'O número {num} foi adicionado na {i} posição.')
                break
        else:
            listaNum.append(num)
            print(f'O número {num} foi adicionado ao final da lista...')
print("-"*30)
for i, v in enumerate(listaNum):
    print(f"{v} na posição {i}")
