# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
nasc = []
idade = []
maior18 = 0
menor18 = 0
for x in range(7):
    nasc.append(int(input(f"Digite o ano de nascimento da {x+1}ª pessoa: ")))
    idade.append(date.today().year - nasc[x])
    if idade[x] >= 18:
        maior18 += 1
    else:
        menor18 += 1
print(f"Voce informou {maior18} pessoa(s) maior(es) de idade. E {menor18} pessoa(s) menores de idade.")
