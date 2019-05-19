# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

pares = []
impares = []
for e in range(1, 8):
    try:
        n = int(input(f'Digite o {e}º valor: '))
        if n % 2 == 0:
            if len(pares) == 0:
                pares.append(n)
            else:
                for i, v in enumerate(pares):
                    if n < v:
                        pares.insert(i, n)
                        break
                else:
                    pares.append(n)

        else:
            if len(impares) == 0:
                impares.append(n)
            else:
                for i, v in enumerate(impares):
                    if n < v:
                        impares.insert(i, n)
                        break
                else:
                    impares.append(n)
    except:
        print('Entrada inválida.')
        continue
print(f'Pares: {pares}')
print(f'Impares: {impares}')