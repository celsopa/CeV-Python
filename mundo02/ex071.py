# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informarquantas cédulas de cada valor serão entregues.

print('*' * 45)
print(f'{"CAIXA ELETRÔNICO":^45}')
print('*' * 45)
# n100 = n50 = n20 = n10 = n5 = n2 = n1 0

while True:
    try:
        saque = int(input('Quanto deseja sacar? R$'))
        n100 = saque // 100
        n50 = (saque % 100) // 50
        n20 = ((saque % 100) % 50) // 20
        n10 = (((saque % 100) % 50) % 20) // 10
        n5 = ((((saque % 100) % 50) % 20) % 10) // 5
        n2 = (((((saque % 100) % 50) % 20) % 10) % 5) // 2
        n1 = ((((((saque % 100) % 50) % 20) % 10) % 5) % 2)
        notas = {
            'R$100.00': n100,
            'R$50.00': n50,
            'R$20.00': n20,
            'R$10.00': n10,
            'R$5.00': n5,
            'R$2.00': n2,
            'R$1.00': n1
        }
        for k, v in notas.items():
            if v != 0:
                print(f'{int(v)} cédulas de {k}')
    except:
        print('ERRO! Entrada inválida.')
        continue
