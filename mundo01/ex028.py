# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
nPC = randint(0,5)
nUser = int(input("Tente advinhar o número escolhido pelo computador [0 a 5]: "))
if nPC == nUser:
    print("Você acertou!")
else:
    print(f"Você errou, o computador escolheu {nPC}")