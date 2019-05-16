# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.

num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
       'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')
print(' - = Número por Extenso = -')
while True:
    try:
        n = int(input('Informe um número de 0 a 20: '))
        while not (0 <= n <= 20):
            n = int(input('Informe um número de 0 a 20: '))
        print('Voce digitou:', num[n].title())
        cont = input("Deseja continuar? [S/N]").strip().upper()[0]
        while cont not in 'SN':
            cont = input("Deseja continuar? [S/N]").strip().upper()[0]
        if cont == 'N':
            break
    except:
        print('ERRO! Entrada inválida.')
        continue
print('Programa Encerrado!')
