# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Informe o valor do imóvel: R$"))
salario = float(input("Informe seu rendimento mensal: "))
anos = int(input("Informe o prazo de pagamento em anos: "))

prestMensal = valorCasa/anos/12
print(f"Para financiar um imóvel de R${valorCasa:.2f} em {anos} anos,\no valor da prestação mensal será de R${prestMensal:.2f}")
if prestMensal <= salario*0.3:
    print("Empréstimo APROVADO!")
else:
    print("O valor da prestação excede 30% do seu salário.\nEmpréstimo NEGADO.")
