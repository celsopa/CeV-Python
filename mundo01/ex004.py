# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input("Digite algo: ")
print(f"O tipo primitivo é: {type(x)}")
print(f"Só tem espaço? {x.isspace()}")
print(f"Contém apenas letras? {x.isalpha()}")
print(f"Contém apenas números? {x.isnumeric()}")
print(f"É alfanumérico? {x.isalnum()}")
print(f"Está em maiúscula? {x.islower()}")
print(f"Está em maiúscula? {x.isupper()}")
print(f"Está capitalizada? {x.istitle()}")

