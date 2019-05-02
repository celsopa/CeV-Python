# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input("Digite um número real: "))
print(f"""O valor digitado foi {num} e sua porção inteira é {int(num)}.""")