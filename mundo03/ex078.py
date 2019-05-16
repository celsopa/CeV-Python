# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = []
for i in range(5):
    num.append(int(input(f'Digite um valor para a posição {i}: ')))
print(f'O MAIOR valor informado: {max(num)}, nas posições: ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i} ', end='')
print()
print(f'O MENOR valor informado: {min(num)}, nas posições: ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i} ', end='')