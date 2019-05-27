from utilidadesCeV.moeda import *

p = float(input('Informe o preço: R$'))
pAumento = int(input('Informe a porcentagem de aumento: '))
pDiminuir = int(input('Informe a porcentagem de desconto: '))
print(f'''A metade de {moeda(p)} é {metade(p, True)}
O dobro de {moeda(p)} é {dobro(p, True)}
Aumentando {pAumento}% de {moeda(p)} = {aumentar(p, pAumento, True)}
Diminuindo {pDiminuir}% de {moeda(p)} = {diminuir(p, pDiminuir, True)}''')