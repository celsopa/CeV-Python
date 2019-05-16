# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input("Informe um valor para ver sua tabuada de multiplicação: "))
print(f"""A tabuada de multiplicação de {n} é:
{'-'*12}
{n} x  1 = {n*1:>3}
{n} x  2 = {n*2:>3}
{n} x  3 = {n*3:>3}
{n} x  4 = {n*4:>3}
{n} x  5 = {n*5:>3}
{n} x  6 = {n*6:>3}
{n} x  7 = {n*7:>3}
{n} x  8 = {n*8:>3}
{n} x  9 = {n*9:>3}
{n} x 10 = {n*10:>3}
{'-'*12}""")