# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
jogadores = {}
for i in range(4):
    jogadores[f'Jogador_{i+1}'] = randint(1, 6)
print('Valores sorteados: ')
for i, v in jogadores.items():
    print(f'{i} tirou {v}')
print(' -=< RANKING >=-')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}')
