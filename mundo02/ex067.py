# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    try:
        n = int(input('Informe um número: '))
        if n < 0:
            break
        print(f"TABUADA DE MULTIPLICAÇÃO DE {n}:")
        for i in range(1, 11):
            print(f'{n:>} x {i:>2} = {n*i}')
    except:
        print('ERRO! Entrada inválida.')
        continue
