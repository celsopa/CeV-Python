# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maiornum(* num):
    print(f'Analisando...')
    sleep(0.5)
    if len(num) == 0:
        print('Não foi informado nenhum valor.')
    else:
        sleep(0.4)
        if len(num) == 1:
            print(f'Foi informado {len(num)} número: ')
        else:
            print(f'Foram informados {len(num)} números: ')
        for i in num:
            sleep(0.3)
            print(f'{i}', end=' ')
        print()
        maior = 0
        for i in range(len(num)):
            if i == 0:
                maior = num[i]
            else:
                if num[i] > maior:
                    maior = num[i]
        sleep(0.8)
        print(f'O maior valor informado é {maior}.')
    print('-=-' * 10)
    sleep(1)


maiornum(2, 9, 4, 5, 7, 1)
maiornum(4, 7, 5)
maiornum(1, 8)
maiornum(6)
maiornum()
