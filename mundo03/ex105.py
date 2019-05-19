# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(* notas, sit=False):
    """
    -> Analisa as várias notas e situaçao de uma turma.
    :param notas: Notas da turma.
    :param sit: (Opcional) Exibe a situação da turma.
    :return: Um dicionário contendo informações da turma.
    """
    maior = menor = soma = qtdnotas = 0
    dicio = {}
    for i in range(len(notas)):
        soma += notas[i]
        qtdnotas += 1
        if i == 0:
            maior = menor = notas[i]
        else:
            if notas[i] > maior:
                maior = notas[i]
            if notas[i] < menor:
                menor = notas[i]
    media = round(soma/qtdnotas, 2)
    if media > 7:
        situacao = 'Boa'
    elif media < 5:
        situacao = 'Ruim'
    else:
        situacao = 'Na média'
    dicio['Quantidade de Notas'] = qtdnotas
    dicio['Maior nota'] = maior
    dicio['Menor nota'] = menor
    dicio['Média da turma'] = media
    if sit:
        dicio['Situação'] = situacao
    return dicio


print(notas(5.5, 9.5, 8, 9.6, 2.5, 8.5, sit=True))
