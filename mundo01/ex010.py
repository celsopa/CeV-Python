# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input("Informe seu saldo em reais: R$"))
cotacao = 3.27
# cotacao = float(input("Informe a cotação do dólar: US$"))  #lê a cotacao do dolar desejada
dolar = carteira/cotacao
print(f"""Com R${carteira:.2f} é possível comprar US${dolar:.2f}.""")