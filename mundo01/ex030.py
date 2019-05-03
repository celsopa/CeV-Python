# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input("Digite um número inteiro: "))
print(f"""Analisando o número {n}...
O número {n} é {'PAR' if n%2==0 else 'ÍMPAR'}.""")
