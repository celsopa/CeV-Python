# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def escreva(texto):
    t = (len(texto)//3) + 4
    print('-=-'*t)
    print(f'      {texto}')
    print(f'-=-' * t)


escreva('YouTube')
escreva('Celso Araújo')