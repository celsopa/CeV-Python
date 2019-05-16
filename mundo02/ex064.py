# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numeros = []
n = 0
while n != 999:
    n = int(input('Digite um número [999 para PARAR]: '))
    if n != 999:
        numeros.append(n)
print()
print(f'Foram digitados {len(numeros)} números.')
print(f'A soma dos números digitados é {sum(numeros)}.')
