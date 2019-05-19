# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
pessoa = {}
mediaIdade = 0
while True:
    try:
        pessoa.clear()
        pessoa['Nome'] = input('Nome: ').strip().title()
        pessoa['Sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if pessoa['Sexo'] not in 'MF':
            print('Entrada inválida. Digite apenas [M]asculino ou [F]emino.')
            pessoa['Sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        pessoa['Idade'] = int(input('Idade: '))
        pessoas.append(pessoa)
        pessoa = pessoa.copy()
        mediaIdade += pessoa['Idade']
        cont = input('Continuar? [S/N] ').strip().upper()[0]
        while cont not in 'SN':
            print('Entrada inválida. Responsa [S]im ou [N]ão.')
            cont = input('Continuar? [S/N] ').strip().upper()[0]
        if cont == 'N':
            break
    except:
        print('ERRO! Entrada Inválida.')
        continue
mediaIdade /= len(pessoas)
print('==='*15)
print(f'=========={"Analisando Cadastro":^25}==========')
print('==='*15)
print(f"""A) Foram cadastradas {len(pessoas)} pessoas.
B) A média de idade é de {mediaIdade:.2f} anos.""")
print('C) Mulheres cadastradas: ', end='')
for p in pessoas:
    if p["Sexo"] == 'F':
        print(f'[{p["Nome"]}]', end=' ')
print()
print('D) Pessoas com idade acima da média:')
for p in pessoas:
    if p['Idade'] > mediaIdade:
        print(f'   Nome: {p["Nome"]:9} | Sexo: {p["Sexo"]} | Idade: {p["Idade"]}')
print(f'=========={"FINALIZADO":^25}==========')
