# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior18 = 0
qtdH = 0
mSub20 = 0

while True:
    try:
        print(' - - CADASTRE UMA PESSOA - -')
        idade = int(input('Digite a idade da pessoa: '))
        sexo = input('Informe o sexo: [M/F]').strip().upper()[0]
        while sexo not in 'MF':
            sexo = input('Informe o sexo: [M/F]').strip().upper()[0]
        if idade > 18:
            maior18 += 1
        if sexo == 'M':
            qtdH += 1
        else:
            if idade < 20:
                mSub20 += 1
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
        while cont not in 'SN':
            cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if cont == 'N':
            break
    except:
        print('ERRO!Entrada inválida.')
        continue
print('-+-'*15)
print(f"""DADOS CADASTRADOS:
Quantidade de pessoas maiores de 18 anos: {maior18}
Quantidade de homens cadastrados: {qtdH}
Quantidade de MULHERES com idade inferior a 20 anos: {mSub20}""")
