def leiadinheiro(msg):
    """
    -> Executa a leitura de um valor monetário, encontrando o caractere separador entre valor inteiro e real.
    :param msg: (String) Mensagem a ser exibida no prompt para o usuário durante a leitura.
    :return: o valor monetário em ponto flutuante.
    """
    n = input(msg).strip()
    if n.isnumeric():
        return float(n)
    for x in n:
        if x.isnumeric() == False:
            sep = x
    n = n.replace(sep, '.')
    return float(n)
