# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: Número inteiro para calcular o fatorial.
    :param show: (Opcional) Exibir o procsso de cálculo. Default=False
    :return: O valor do fatorial de um número [num].
    """
    print('~'*30)
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            if i == 1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
    return f


help(fatorial)
print(fatorial(5, show=True))