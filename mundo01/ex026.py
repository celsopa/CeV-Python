# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ").strip().lower()
a = frase.count('a')
print(f"""Analisando a frase...
A letra 'a' aparece {frase.count('a')} vezes.
Sua primeira aparição é na posição {frase.find('a')+1}.
Sua última aparição é na posição {frase.rfind('a')+1}.""")
