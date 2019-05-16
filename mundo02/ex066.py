# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

numeros = []
while True:
    try:
        n = int(input('Digite um número [999 para PARAR]: '))
        if n != 999:
            numeros.append(n)
        else:
            break
    except:
        print('ERRO! Entrada inválida!')
        continue
print()
print(f'Foram digitados {len(numeros)} números.')
print(f'A soma dos números digitados é {sum(numeros)}.')
