# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from utilidadesCeV.moeda import *

p = float(input('Informe o preço: R$'))
pAumento = int(input('Informe a porcentagem de aumento: '))
pDiminuir = int(input('Informe a porcentagem de desconto: '))
print(f'''A metade de {p} é {metade(p)}
O dobro de {p} é R${dobro(p)}
Aumentando {pAumento}% de {p} = {aumentar(p, pAumento)}
Diminuindo {pDiminuir}% de {p} = {diminuir(p, pDiminuir)}''')
