from utilidadesCeV.moeda import *

p = float(input('Informe o preço: R$'))
pAumento = int(input('Informe a porcentagem de aumento: '))
pDiminuir = int(input('Informe a porcentagem de desconto: '))
print(f'''A metade de {moeda(p)} é {moeda(metade(p))}
O dobro de {moeda(p)} é R${moeda(dobro(p))}
Aumentando {moeda(pAumento)}% de {moeda(p)} = {moeda(aumentar(p, pAumento))}
Diminuindo {moeda(pDiminuir)}% de {moeda(p)} = {moeda(diminuir(p, pDiminuir))}''')
