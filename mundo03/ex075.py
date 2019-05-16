# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = tuple(int(input("Digite um número: ")) for i in range(4))

print(f"Números digitados: {num}")
print(f"Você digitou [9] {num.count(9)} vezes.")
print(f"O número [3] foi digitado na {(num.index(3)+1) if 3 in num else 'N/A'}ª posição.")
print(f"Os números pares digitaos foram: {list(filter(lambda x: x % 2 == 0, num))}.")
