# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('Verificando a situação do aluno...')
if (n1 + n2) / 2 >= 7:
    print(f'Aluno APROVADO, com média {(n1 + n2) / 2:.2f}')
elif (n1 + n2) / 2 < 5:
    print(f'Aluno REPROVADO, com média {(n1 + n2) / 2:.2f}')
else:
    print(f'Aluno EM RECUPERAÇÃO, com média {(n1 + n2) / 2:.2f}')
