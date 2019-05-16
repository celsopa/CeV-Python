# Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

i = 0
soma = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        i += 1
        soma += x
print(f"A soma dos {i} valores ímpares múltiplos de 3 entre 1 e 500 é igual a {soma}.")