# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o preço do produto: R$"))
print(f"""FORMAS DE PAGAMENTO:
[ 1 ] - à vista dinheiro/cheque
[ 2 ] - à vista no cartao
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão""")
condicao = int(input("Informe a condição de pagamento: "))
if condicao == 1:
    print(f"Sua compra de R${preco:.2f} vai custar R${preco*0.9:.2f} no final.")
elif condicao == 2:
    print(f"Sua compra de R${preco:.2f} vai custar R${preco*0.95:.2f} no final.")
elif condicao == 3:
    print(f"Sua compra será parcelada em 2x de R${preco/2:.2f}, sem juros.")
    print(f"Sua compra de R${preco:.2f} vai custar R${preco:.2f} no final.")
elif condicao == 4:
    parcelas = int(input("Quantas parcelas? "))
    print(f"Sua compra será parcelada em {parcelas}x de R${preco*1.2/parcelas:.2f}, sem juros.")
    print(f"Sua compra de R${preco:.2f} vai custar R${preco*1.2:.2f} no final devido aos juros.")
else:
    print(f"Condição de pagamento inválida!")
