# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
lista = list([input("Aluno 1: "), input("Aluno 2: "), input("Aluno 3: "), input("Aluno 4: ")])
shuffle(lista)
print(f"""A ordem de apresentação é: 1º: {lista[0]}, 2º: {lista[1]}, 3º: {lista[2]}, 4º: {lista[3]}.""")
