# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Informe o número em que o carro foi alugado: "))
km = float(input("Informe a distância percorrida com o veículo: "))
preco = dias*60 + km*0.15
print(f"""O carro foi alugado por {dias} dias e rodou {km} kilometros.
O total a pagar é de R$ {preco:.2f}""")