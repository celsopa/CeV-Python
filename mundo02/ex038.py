# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print(f"Analisando os números {n1} e {n2}...")
if n1>n2:
    print(f"""O maior número é: {n1}""")
elif n2>n1:
    print(f"""O maior número é: {n2}""")
else:
    print(f"Os números digitados são iguais.")
