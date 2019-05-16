# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

produtos = ('Lápis', 0.65,
            'Borracha', 0.40,
            'Caderno', 4.50,
            'Estojo', 3.45,
            'Transferidor', 3.75,
            'Compasso', 2.50,
            'Mochila', 34.00,
            'Caneta', 1.25,
            'Livro', 45.00)

print('='*30)
print(f'{"LISTA DE PREÇOS":^30}')
print('='*30)
for i in range(0, len(produtos),    2):
    print(f' {produtos[i]:.<20}R${produtos[i+1]:>6.2f}')