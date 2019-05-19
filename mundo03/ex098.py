# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contagem(inicio, final, passo):
    if final > inicio:
        tam = ((final - inicio) // passo) + 1
        print(f'-=-' * tam)
        print(f'Contagem de {inicio} a {final}, de {passo} em {passo}:')
        sleep(2)
        for i in range(inicio, final + 1, passo):
            print(f'{i} ', end='')
            sleep(0.7)
        print('FIM')
    else:
        tam = ((inicio - final) // passo) + 1
        print(f'-=-' * tam)
        print(f'Contagem de {inicio} a {final}, de {passo} em {passo}:')
        sleep(2)
        for i in range(inicio, final - 1, -passo):
            print(f'{i} ', end='')
            sleep(0.7)
        print('FIM')
    print(f'-=-' * tam)


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez. Escolha')
ini = int(input('Inicio: '))
fim = int(input('Final:  '))
pas = int(input('Passo:  '))
if pas < 0:
    pas = -pas
elif pas == 0:
    pas = 1
contagem(ini, fim, pas)
