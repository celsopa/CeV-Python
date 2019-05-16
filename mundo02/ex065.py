# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = int(input('Digite um número: '))
maior = n
menor = n
soma = 0
soma += n
qtd = 1
while True:
    cont = input('Deseja continuar? [S/N]').strip().upper()[0]
    while cont not in "SN":
        cont = input('Deseja continuar? [S/N]').strip().upper()[0]
    if cont == 'N':
            break
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    qtd += 1
print()
print(f'''Foram digitados {qtd} números.
O MAIOR valor foi {maior}. E o MENOR valor foi {menor}.
A SOMA dos números digitados é {soma}.
A MÉDIA dos números digitados é {soma/qtd}.''')