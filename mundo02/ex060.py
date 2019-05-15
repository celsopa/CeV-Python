# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

print("Calculando Fatorial")
n = int(input("Digite um número inteiro: "))
fat = 1

if n >=0:
    print(f"Calculando {n}! = ", end='')
    while n > 0:
        print(f"{n} x " if n > 1 else f"{n} = ", end='')
        fat *= n
        n -= 1
    print(f"{fat}")
else:
    print("Não pode ser calculado!")