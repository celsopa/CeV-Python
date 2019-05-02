# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
al1 = input("Digite o nome do primeiro aluno: ")
al2 = input("Digite o nome do segundo aluno: ")
al3 = input("Digite o nome do terceiro aluno: ")
al4 = input("Digite o nome do quarto aluno: ")
sala = [al1, al2, al3, al4]
escolhido = choice(sala)
print(f"O aluno escolhido foi: {escolhido.title()}")
