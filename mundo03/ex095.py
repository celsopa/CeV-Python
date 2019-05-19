# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
time = []
while True:
    try:
        jogador['Nome'] = input('Nome do jogador: ').strip().title()
        partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
        jogador['Gols'] = []
        for i in range(partidas):
            jogador['Gols'].append(int(input(f'Quantos gols na partida {i + 1}: ')))
        jogador['Total de gols'] = sum(jogador['Gols'])
        time.append(jogador.copy())
        cont = input('Continuar [S/N]:  ').strip().upper()[0]
        while cont not in "SN":
            print('Entrada inválida. Digite apenas S ou N')
            cont = input('Continuar [S/N]:  ').strip().upper()[0]
        if cont == 'N':
            break
    except:
        print('ERRO. Entrada Inválida.')
        continue
print('-=-'*18)
print(f'-------{"Analisando Equipe":^40}-------')
print('-=-'*18)
print(f"{'cód':^5}|{'Jogador':^10}|{'Total de Gols':^15}|{'Gols':^6}")
for i in range(len(time)):
    print(f"{i:5}|{time[i]['Nome']:10}|{time[i]['Total de gols']:15}|{time[i]['Gols']}")
while True:
    try:
        print('999 para PARAR')
        mostrar = int(input('Mostrar dados de qual jogador [cód]: '))
        while (mostrar > (len(time)-1) or mostrar < 0) and mostrar != 999:
            print(f'Código inválido. Não existe jogador com o código {mostrar}')
            print('-'*54)
            print('999 para PARAR')
            mostrar = int(input('Mostrar dados de qual jogador [cód]: '))
        if mostrar == 999:
            print('Encerrando...')
            break
        print(f'EXIBINDO DADOS DE {time[mostrar]["Nome"]}: ')
        for i in range(len(time[mostrar]["Gols"])):
            print(f'    Na partida {i+1} marcou {time[mostrar]["Gols"][i]} gol(s).')
        print('-'*54)
    except:
        print('ERRO. Entrada inválida.')
        continue
