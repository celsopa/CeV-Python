# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totalGasto = 0
menorPreco = 99999999999999999999
produtoBarato = ''
mais1000 = 0

while True:
    try:
        prod = input('Informe o produto: ').strip()
        preco = float(input('Informe o preço: '))
        totalGasto += preco
        if preco > 1000:
            mais1000 += 1
        if preco < menorPreco:
            menorPreco = preco
            produtoBarato = prod

        cont = input('Deseja continuar? [S/N]').strip().upper()[0]
        while cont not in "NS":
            cont = input('Deseja continuar? [S/N]').strip().upper()[0]
        if cont == 'N':
            break
    except:
        print('ERRO! Entrada inválida.')
        continue
print(f"""ANALISANDO PRODUTOS...
Você gastou um total de R${totalGasto:.2f}
Você comprou {mais1000} produtos acima de R$1.000,00
O produto mais barato foi [{produtoBarato}] e custou R${menorPreco:.2f}""")
