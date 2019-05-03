# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Informe o salário do funcionário: R$"))
if sal > 1250:
    sal *= 1.1
else:
    sal *= 1.15
print(f"""O funcionário teve um aumento de {'10' if sal>1250 else '15'}%.
O novo salário desse funcionário é {sal:.2f}.""")
