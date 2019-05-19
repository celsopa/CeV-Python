# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
while True:
    try:
        nome = input('Nome do usuário: ').strip().title()
        peso = float(input(f'Peso de {nome}: '))
        pessoas.append((peso, nome))
        cont = input('Informar outro usuário? [S/N] ').strip().upper()[0]
        while cont not in "SN":
            cont = input('Informar outro usuário? [S/N] ').strip().upper()[0]
        if cont == 'N':
            break
    except:
        print('ERRO! Entrada inválida.')
        continue
print(f"""Analisando...
Quantidade de pessoas cadastradas: {len(pessoas)}""")
print(f'A(s) pessoa(s) mais pesada(s), com {sorted(pessoas, reverse=True)[0][0]}Kg é: ', end='')
for x in pessoas:
    if x[0] == sorted(pessoas, reverse=True)[0][0]:
        print(f'[{x[1]}]', end='  ')
print(f'\nA(s) pessoa(s) mais leve(s), com {sorted(pessoas)[0][0]}Kg é: ', end='')
for x in pessoas:
    if x[0] == sorted(pessoas)[0][0]:
        print(f'[{x[1]}]', end='  ')
