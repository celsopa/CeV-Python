# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input("Digite a distância da viagem: "))
print("Você percorrerá {dist}km.")
if dist <= 200:
    print(f"O preço da sua passagem é R${dist*0.5:.2f}")
else:
    print(f"O preço da sua passagem é R${dist*0.45:.2f}")
