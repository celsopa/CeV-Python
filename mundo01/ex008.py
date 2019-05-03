# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

dist = float(input("Digite a distância em metros: "))
km = dist/1000
hm = dist/100
dam = dist/10
dm = dist*10
cm = dist*100
mm = dist*1000

print(f"""Kilometros: {km}
Hectometros: {hm}
Decametros: {dam}
decimetros: {dm:.0f}
centimetros: {cm:.0f}
milimetros: {mm:.0f}""")