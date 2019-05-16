# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = input("Digite uma frase: ").strip().lower()
teste = ''
for x in frase:
    if x.isalpha():
        teste += x

if teste == teste[::-1]:
    print("A frase digitada é um palíndromo!")
else:
    print("A frase digitada NÃO é um palíndromo!")