# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
i = 0
for x in range(6):
    n = int(input(f"Digite {x}º número inteiro: "))
    if n % 2 == 0:
        soma += n
        i += 1
print(f"A soma dos {i} números pares digitados é {soma}.")