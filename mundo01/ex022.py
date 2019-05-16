# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).

nome = input("Digite seu nome completo: ").strip()
lstNome = nome.split(" ")
nomeSemEspaco = "".join(lstNome)
print(f"Analisando o nome '{nome.title()}'... \n"
f"Em maiúsculas é: {nome.upper()}\n"
f"Em minúsculas é: {nome.lower()}\n"
#f"Quantidade de letras: {len(nomeSemEspaco)}\n"
f"Quantidade de letras: {len(nome)- nome.count(' ')}\n"
f"Seu primeiro nome: '{lstNome[0].title()}' e ele tem {len(lstNome[0])} letras")
