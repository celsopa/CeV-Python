# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e
# os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
while True:
    try:
        n = int(input('Digite um número: '))
        lista.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
        cont = input('Continuar? [S/N] ').strip().upper()[0]
        while cont not in 'SN':
            cont = input('Continuar? [S/N] ').strip().upper()[0]
        if cont == 'N':
            break
    except:
        print('ERRO. Entrada inválida.')
        continue
print('~'*30)
print(f"""Lista completa: {sorted(lista)}
Lista dos PARES: {sorted(pares)}
Lista dos IMPARES: {sorted(impares)}""")
