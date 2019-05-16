# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 'a'
while sexo not in "MF":
    sexo = input("Informe seu sexo [M/F]: ").strip().upper()[0]
    if sexo == "M":
        print(f"O sexo cadastrado foi: MASCULINO")
    elif sexo == "F":
        print(f"O sexo cadastrado foi: FEMININO")
    else:
        print("Sexo inválido. Tente novamente.")
