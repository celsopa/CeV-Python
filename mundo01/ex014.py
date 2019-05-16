# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempC = float(input("Informe a temperatura em ºC: "))
tempF = (tempC * 1.8) + 32
print(f"""A temperatura {tempC:.1f} ºC equivale a {tempF:.1f} ºF.""")