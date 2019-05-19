# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
cadastro = {}
cadastro['Nome'] = input('Nome: ').strip().title()
cadastro['Idade'] = date.today().year - int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('Número da CTPS [0 caso não tenha]: '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Contratação'] + 35 - date.today().year)
print('~'*30)
for k, v in cadastro.items():
    print(f'{k} → {v}')