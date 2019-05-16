# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lisNum = []
while True:
    try:
        num = int(input('Digite um número: '))
        if num not in lisNum:
            lisNum.append(num)
            print('Número adicionado com sucesso...')
        else:
            print('O número informado já existe na lista.')
        cont = input('Deseja continuar? [S/N]').strip().upper()[0]
        while cont not in 'SN':
            cont = input('Deseja continuar? [S/N]').strip().upper()[0]
        if cont == 'N':
            break
    except:
        print('ERRO! Entrada inválida.')
        continue
print(f'Lista de números digitaos: {sorted(lisNum)}')