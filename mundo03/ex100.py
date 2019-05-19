# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(inic=1, fim=10, qtd=2):
    print(f'Gerando lista com {qtd} elementos, no intervalos de {inic} a {fim}:')
    lista = []
    for i in range(qtd):
        sleep(0.4)
        lista.append(randint(inic, fim))
        print(lista[i], end=' ')
    print()
    return lista


def somapar(l):
    print(f'Analisando a lista...')
    sleep(1)
    soma = 0
    for i in l:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos números PARES informados é: {soma}.')


somapar(sorteia(3, 8, 3))
