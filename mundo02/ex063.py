# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci.

ant = 0
suc = 1
soma = ant + suc

print(f'{"SEQUENCIA DE FIBONACCI":^45}')
print('-=-'*15)

termos = int(input("Quantos termos você quer mostrar? "))
if termos == 1:
    print(ant, end=" \u2192 ")
elif termos == 2:
    print(ant, end=" \u2192 ")
    print(suc, end=" \u2192 ")
else:
    print(ant, end=" \u2192 ")
    print(suc, end=" \u2192 ")
    for i in range(termos-2):
        print(soma, end=" \u2192 ")
        ant = suc
        suc = soma
        soma = ant + suc
print('FIM')
