# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
print(f"""Suas opções:
[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA""")
maoUser = int(input("Qual sua opção: "))
maoPC = randint(1, 3)

if maoUser == 1:
    if maoPC == 1:
        print("O computador escolheu PEDRA e você PEDRA. EMPATE.")
    elif maoPC == 2:
        print("O computador escolheu PAPEL e você PEDRA. VOCÊ PERDEU.")
    else:
        print("O computador escolheu TESOURA e você PEDRA. VOCÊ GANHOU.")
elif maoUser == 2:
    if maoPC == 1:
        print("O computador escolheu PEDRA e você PAPEL. VOCÊ GANHOU.")
    elif maoPC == 2:
        print("O computador escolheu PAPEL e você PAPEL. EMPATE.")
    else:
        print("O computador escolheu TESOURA e você PAPEL. VOCÊ PERDEU.")
elif maoUser == 3:
    if maoPC == 1:
        print("O computador escolheu PEDRA e você TESOURA. VOCÊ PERDEU.")
    elif maoPC == 2:
        print("O computador escolheu PAPEL e você TESOURA. VOCÊ GANHOU.")
    else:
        print("O computador escolheu TESOURA e você TESOURA. EMPATE.")
else:
    print("OPÇÃP INVÁLIDA!")
