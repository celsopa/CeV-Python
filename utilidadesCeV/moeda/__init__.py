def aumentar(preco, porc, sifrao=False):
    """
    -> Calcula o valor aumentado em determinada porcentagem.
    -> Pode exibir ou não o sinal de sifrão.
    :param preco: numero real a ser aumentado
    :param porc: porcentagem de incremento. Ex: 4 para 4% | 10 para 10% | 27 para 27%
    :param sifrao: (opcional) Define se será exibido ou não o sinal de sifrão. Padrão é False
    :return: retorna o valor aumentado na porcentagem informada
    """
    preco = preco + ((preco*porc)/100)
    if sifrao:
        return moeda(preco)
    return preco


def diminuir(preco, porc, sifrao=False):
    """
    -> Calcula o valor diminuído em determinada porcentagem.
    -> Pode exibir ou não o sinal de sifrão.
    :param preco: numero real a ser diminuído
    :param porc: porcentagem de decremento. Ex: 4 para 4% | 10 para 10% | 27 para 27%
    :param sifrao: (opcional) Define se será exibido ou não o sinal de sifrão. Padrão é False
    :return: retorna o valor diminuido na porcentagem informada
    """
    preco = preco - ((preco * porc) / 100)
    if sifrao:
        return moeda(preco)
    return preco


def dobro(preco, sifrao=False):
    """
    -> Calcula o dobro de um valor.
    -> Pode exibir ou não o sinal de sifrão.
    :param preco: numero real a dobrado
    :param sifrao: (opcional) Define se será exibido ou não o sinal de sifrão. Padrão é False
    :return: o dobro de um valor real
    """
    if sifrao:
        return moeda(preco*2)
    return preco*2


def metade(preco, sifrao=False):
    """
    -> Calcula a metade de um valor.
    -> Pode exibir ou não o sinal de sifrão.
    :param preco: numero real a diminuido pela metade
    :param sifrao: (opcional) Define se será exibido ou não o sinal de sifrão. Padrão é False
    :return: a metade de um valor real
    """
    if sifrao:
        return moeda(preco/2)
    return preco/2


def moeda(valor, sifrao=True):
    """
    -> Exibe o sinal de sifrão para um número informado.
    :param valor: valor a ser precedido do sifrão
    :return: sifrão acrescido do valor
    """
    if sifrao == False:
        return f'{valor:.2f}'
    return f'R${valor:.2f}'.replace('.', ',')


def resumo(preco, pAum=0, pDec=0, sifrao=True):
    """
    -> Exibi um resumo de 'dobro', 'metade', 'aumento' e 'desconto' de um valor.
    -> Pode exibir o sinal de sifrão.
    :param preco: valor real a ser analisado
    :param pAum: porcentagem de aumento. Ex: 4 para 4% | 10 para 10% | 27 para 27%
    :param pDec: porcentagem de desconto. Ex: 4 para 4% | 10 para 10% | 27 para 27%
    :param sifrao: (Opcional) Exibe o sinal de sifrão. Padrão é True
    :return: retorna uma tabela com as informações 'preço', 'dobro', 'metade', 'aumento' e 'desconto'
    """
    print('=' * 40)
    print(f'{"Resumo do Valor":^40}')
    print('-' * 40)
    print(f"{'Preço Analisado:':<20}{moeda(preco, sifrao):>20}")
    print(f"{'Dobro do preço:':<20}{dobro(preco, sifrao):>20}")
    print(f"{'Metade do preço:':<20}{metade(preco, sifrao):>20}")
    print(f"{f'{pAum}% de aumento':<20}{aumentar(preco, pAum, sifrao):>20}")
    print(f"{f'{pDec}% de desconto':<20}{diminuir(preco, pDec, sifrao):>20}")
    print('=' * 40)



    # print('=' * 40)
    # print(f'{"Resumo do Valor":^40}')
    # print('-' * 40)
    # valor = moeda(preco, sifrao)
    # pDobro = dobro(preco, sifrao)
    # pMetade = metade(preco, sifrao)
    # aumento = aumentar(preco, pAum, sifrao)
    # desconto = diminuir(preco, pDec, sifrao)
    # print(f"{'Preço Analisado:':<20}{valor:>20}")
    # print(f"{'Dobro do preço:':<20}{pDobro:>20}")
    # print(f"{'Metade do preço:':<20}{pMetade:>20}")
    # print(f"{f'{pAum}% de aumento':<20}{aumento:>20}")
    # print(f"{f'{pDec}% de desconto':<20}{desconto:>20}")
    # print('=' * 40)