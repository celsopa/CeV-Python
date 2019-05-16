# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Informe seu nome completo: ").strip().split()
print(f'''Analisando o nome...
O pronome é: "{nome[0]}"
O (último) sobrenome é: "{nome[-1]}"''')
