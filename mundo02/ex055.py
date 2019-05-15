# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso = float(input("Informe o peso da 1ª pessoa: "))
maior = peso
menor = peso
for x in range(2, 6):
    x = float(input(f"Informe o peso da {x}ª pessoa: "))
    if x < menor:
        menor = x
    elif x > maior:
        maior = x
print(f"""O maior peso informado é {maior}Kg. E o menor peso foi {menor}Kg.""")
