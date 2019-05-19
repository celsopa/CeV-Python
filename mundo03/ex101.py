# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade >= 18:
        print('Voto OBRIGATÓRIO.')
    elif idade < 16:
        print('Voto NEGADO.')
    else:
        print('Voto OPCIONAL.')


ano = int(input('Informe o ano de seu nascimento: '))
voto(ano)
