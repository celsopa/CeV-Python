# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

print(f"A média entre {n1:.1f} e {n2:.1f} é {(n1+n2)/2:.1f}.")