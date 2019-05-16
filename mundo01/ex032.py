# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input("Informe um ano qualquer [0 para o ano atual]: "))
if ano:
    if ano % 400 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é BISSEXTO.")
    else:
        print(f"O ano {ano} NÃO é BISSEXTO.")
else:
    ano = date.today().year
    if ano % 400 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é BISSEXTO.")
    else:
        print(f"O ano {ano} NÃO é BISSEXTO.")
