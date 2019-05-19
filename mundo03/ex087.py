# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
soma = soma3coluna = maior2linha = 0
print('Vamor preencher uma matriz 3 x 3:')
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para a posição {i+1}x{j+1}: '))
        matriz[i].append(n)
print("~"*40)
print('A matriz informada é:')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]:^5}', end=" ")
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            soma3coluna += matriz[i][2]
        if matriz[1][j]:
            if j == 1:
                maior2linha = matriz[1][0]
            else:
                if matriz[1][j] > maior2linha:
                    maior2linha = matriz[1][j]
    print()
print("~"*40)
print(f'''A) A soma de todos os valores pares digitados: {soma}
B) A soma dos valores da terceira coluna: {soma3coluna}
C) O maior valor da segunda linha: {maior2linha}''')