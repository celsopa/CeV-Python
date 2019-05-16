# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print("GERADOR DE PA")
t1 = int(input("Primeiro termo da Progressão Aritmética: "))
r = int(input("RAZÃO da Progressão Aritmética: "))
t = 0
while t < 10:
    print(f"{t1 + (r*t)}", end=" \u2192 ")
    t += 1
resp = 's'
while resp:
    resp = int(input("Quantos termos mais você quer mostrar [ 0 para sair ]? "))
    termos = resp
    while termos > 0:
        print(f"{t1 + (r * t)}", end=" \u2192 ")
        t += 1
        termos -= 1
print('FIM!')