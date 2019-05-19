# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import sample
from time import sleep

jogo = []
qtdPalpites = int(input('Quantos jogos você quer sortear? '))

for i in range(qtdPalpites):
    jogo.append(sample(range(1, 60), 6))
    jogo[i].sort()

print(f'-=<{{   SORTEANDO {qtdPalpites} JOGOS   }}>=-')
for i in range(len(jogo)):
    print(f'Jogo {i+1}: {jogo[i]}')
    sleep(0.8)
