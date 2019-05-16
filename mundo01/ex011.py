# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input("Informe a largura da parede: "))
alt = float(input("Informe a altura da parede: "))
litros = (larg*alt)/2
print(f"""Sua parede tem dimensão de {larg} x {alt} e área de {larg*alt:.2f}m2.
Para pintar a parede informada é preciso {litros:.2f}l de tinta.""")