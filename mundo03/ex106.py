# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores.

def ajuda():
    from time import sleep
    while True:
        print('\033[1;107m-==-\033[m' * 10)
        print(f'\033[1;107m{"Sistema de Ajuda do Python":^40}\033[m')
        print('\033[1;107m-==-\033[m' * 10)
        termo = input(f'Termo de pesquisa> ')
        if termo in 'quit()':
            print(f'\033[1;41m{"Programa Finalizado":^40}\033[m')
            break
        else:
            sleep(0.5)
            print('\033[1;44m~~~~\033[m' * 10)
            busca = f'Pesquisando o termo {termo}'
            print(f'\033[1;44m{busca:^40}\033[m')
            print('\033[1;44m~~~~\033[m' * 10)
            sleep(1)
            print(f'\033[7;30m')
            help(termo)
        sleep(1)


ajuda()
