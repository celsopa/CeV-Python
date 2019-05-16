# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("GERADOR DE PA")
t1 = int(input("Primeiro termo da Progressão Aritmética: "))
r = int(input("RAZÃO da Progressão Aritmética: "))
t = 0
while t < 10:
    print(f"{t1 + (r*t)}", end=" \u2192 ")
    t += 1
print('FIM!')
