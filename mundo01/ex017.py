# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

cat1 = float(input("Informe o comprimento do primeiro cateto: "))
cat2 = float(input("Informe o comprimento do segundo cateto: "))

print(f"""O triângulo retângulo formado pelos catetos {cat1} e {cat2} tem hipotenusa medindo {((cat1**2)+(cat2**2))**(1/2):.2f}""")
