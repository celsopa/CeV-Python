# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador['Nome'] = input('Nome do jogador: ').strip().title()
# jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou?' ))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?' ))
jogador['Gols'] = []
for i in range(partidas):
    jogador['Gols'].append(int(input(f'Quantos gols na partida {i + 1}: ')))
jogador['Total de gols'] = sum(jogador['Gols'])
print('-=-'*20)
print(f'----------{"Analisando Jogador":^40}----------')
print('-=-'*20)
for k, v in jogador.items():
    print(f'{k} → {v}')
print('---'*20)
print(f'O jogador {jogador["Nome"]} particiou de {partidas} partidas.')
for i in range(0, len(jogador['Gols'])):
    print(f'    → Na partida {i+1} marcou {jogador["Gols"][i]} gols.')
if len(jogador['Gols']) != 0:
    print(f'Um total de {jogador["Total de gols"]} gols e uma média de '
          f'{sum(jogador["Gols"])/len(jogador["Gols"]):.1f} gols por partida.')
