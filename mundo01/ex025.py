# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Informe seu nome completo: ").strip().lower()
print(f"A pessoa informada é da família SILVA? {'silva'in nome.split()}")