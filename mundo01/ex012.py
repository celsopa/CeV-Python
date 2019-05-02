# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Informe o preço do produto: R$"))
print(f"""O produto que custava R${preco} terá desconto de 5%.
Seu novo preço é R${preco*0.95:.2f}.""")