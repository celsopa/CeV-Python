# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.

from random import randint

print("Olá, estou pensando em um número inteiro de 0 a 10, tente advinhar qual...")
nPC = randint(0, 10)
print(nPC)
nUser = int(input("Escolha seu número: "))
i = 1
while nUser != nPC:
    i += 1
    nUser = int(input("Você errou. Escolha outro número: "))
print(f"Você acertou o número escolhido pelo computador na {i}ª tentativa.")
