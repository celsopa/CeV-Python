# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    try:
        n = int(input('Digite um número: '))
        lista.append(n)
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
        while cont not in "SN":
            cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if cont == 'N':
            break
    except:
        print('ERRO! Entrada Inválida.')
        continue
print('-=-'*10)
print(f"""ANALISANDO...
Foram digitados {len(lista)} números:
Os valores em ordem decrescente são: {list(i for i in sorted(lista, reverse=True))}""")
if 5 in lista:
    print(f'O valor [5] foi digitado {lista.count(5)} vezes.')
else:
    print('O valor [5] não está na lista.')