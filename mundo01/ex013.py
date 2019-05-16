# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Informe o salário do funcionário: R$'))
print(f"""Um funcionário que recebe R${sal} terá aumento de 15%.
Seu novo salário será R${sal*1.15:.2f}""")
