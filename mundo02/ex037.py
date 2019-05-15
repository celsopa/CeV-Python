# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input("Digite um número inteiro qualquer: "))
print(f"""--- MENO DE CONVERSÃO ---
[1] Binário
[2] OCTAL
[3] HEXADECIMAL""")
base = int(input("Escolha a base de conversão: "))
if base == 1:
    print(f"O decimal {n} para Binário é: {bin(n).strip('0b').upper()}")
elif base == 2:
    print(f"O decimal {n} para Octal é: {oct(n).strip('0c').upper()}")
elif base == 3:
    print(f"O decimal {n} para Hexadecimal é: {hex(n).strip('0x').upper()}")
else:
    print("Base inválida!")
