# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input("Informe uma cidade: ").strip().lower()
comeco = cidade[0:cidade.find(' ')]
print(f"""A cidade informada começa com 'santo'? {cidade == 'santo' or comeco=='santo'}""")
