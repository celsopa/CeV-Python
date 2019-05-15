# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint
print('-=-'*15)
print(f'{"PAR ou ÍMPAR":^45}')
print('-=-'*15)
vit = 0
while True:
    try:
        nPC = randint(0, 10)
        nUser = int(input('Escolha um número: '))
        opcao = input('Par ou Impar? ').strip().upper().upper()[0]
        while opcao not in 'PI':
            opcao = input('Par ou Impar? ').strip().upper().upper()[0]
        if opcao == 'P':
            if (nPC + nUser)%2 == 0:
                print('VOCÊ VENCEU')
                print(f'O computador escolheu {nPC} e você {nUser}.')
                vit += 1
            else:
                print('VOCÊ PERDEU')
                print(f'O computador escolheu {nPC} e você {nUser}.')
                print(f'Você conseguiu vencer {vit} vez(es).')
                break
        else:
            if (nPC + nUser) % 2 != 0:
                print('VOCÊ VENCEU')
                print(f'O computador escolheu {nPC} e você {nUser}.')
                vit += 1
            else:
                print('VOCÊ PERDEU')
                print(f'O computador escolheu {nPC} e você {nUser}.')
                print(f'Você conseguiu vencer {vit} vez(es).')
                break
    except:
        print('ERRO! Entrada inválida.')
        continue