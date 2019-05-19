# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

classe = []

while True:
    try:
        nome = input('Nome do Aluno: ').strip().title()
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        classe.append([nome, nota1, nota2, (nota1+nota2)/2])
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
        while cont not in 'SN':
            cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if cont == "N":
            break
    except:
        print('ERRO! Entrada inválida.')
        continue
print('-=-'*20)
print(f"{'id':^4}|{'Nome':<10}|{'Média':<7}")
print('-'*23)
for i, v in enumerate(classe):
    print(f"{i:^4}|{v[0]:<10}|{v[3]:<7.2f}")
while True:
    try:
        matr = int(input('Deseja visualizar as notas de qual aluno? (999 finaliza): '))
        if matr == 999:
            print(' -=<  PROGRAMA FINALIZADO  >=-')
            break
        print(f'Notas de {classe[matr][0]} : {classe[matr][1]} e {classe[matr][2]}')
        print('-'*23)
    except:
        print('ERRO. Informe um [id] válido')
        continue
