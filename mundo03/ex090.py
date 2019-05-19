# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['Nome'] = input('Nome: ').strip().title()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif aluno['Media'] < 5:
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao'] = 'Em Recuperação'
print('-=-'*10)
for k, v in aluno.items():
    print(f'* {k}: {v}')
