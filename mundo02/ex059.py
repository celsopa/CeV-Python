# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input("Informe o primeiro número inteiro: "))
n2 = int(input("Informe o segundo número inteiro: "))
opc = 0
while opc != 5:
    print(f"""O QUE DESEJA FAZER?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opc = int(input("Escolha uma opção: "))
    if opc == 1:
        print(f"SOMA: {n1} + {n2} = {n1+n2}")
    elif opc == 2:
        print(f"MULTIPLICAÇÃO: {n1} * {n2} = {n1 * n2}")
    elif opc == 3:
        if n1 > n2:
            print(f"MAIOR: {n1} > {n2}")
        elif n2 > n1:
            print(f"MAIOR: {n2} > {n1}")
        else:
            print("Os números são iguais.")
    elif opc == 4:
        n1 = int(input("Informe o primeiro número inteiro: "))
        n2 = int(input("Informe o segundo número inteiro: "))
    elif opc == 5:
        print("Finalizando o programa...")
        continue
    else:
        print(f"""OPÇÃO INVÁLIDA""")
