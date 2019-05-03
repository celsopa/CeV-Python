# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input(f'Informe um número entre 0 e 9999: '))
m = n // 1000
c = n % 1000 // 100
d = n % 100 // 10
u = n % 10
# m = n // 1000 % 10
# c = n // 100 % 10
# d = n // 10 % 10
# u = n // 1 % 10
print(f'Analisando o número {n}...\n'
      f'Unidade: {u}\n'
      f'Dezena: {d}\n'
      f'Centena: {c}\n'
      f'Milhar: {m}')

