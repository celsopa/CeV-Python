# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e
# preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para a posição {i+1}x{j+1}: '))
        matriz[i].append(n)

print('A matriz informada é:')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]:^5}', end=" ")
    print()