# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

t1 = int(input("Primeiro termo da Progressão Aritmética: "))
r = int(input("RAZÃO da Progressão Aritmética: "))
for t in range(10):
    print(f"{t1 + (r*t)}", end=" \u2192 ")
print('ACABOU!')

# Segundo modo do laço FOR
for x in range(t1, t1+10*r, r):
    print(x, end=" \u2192 ")
print('ACABOU!')
