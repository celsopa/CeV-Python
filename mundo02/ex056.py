# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

from time import sleep
pessoas = []
somaIdade = 0
fSub20 = 0
idadeHomemVelho = 0
hVelho = ''
for x in range(4):
    pessoas.append({'nome':input("Informe o nome: ").strip(),
           'idade': int(input("Informe a idade: ")),
           'sexo':input("Informe o sexo [M/F]").upper()[0]})
    somaIdade += pessoas[x]['idade']
    if pessoas[x]['sexo'] == "F" and pessoas[x]['idade'] < 20:
        fSub20 += 1
    if pessoas[x]['sexo'] == "M":
        if pessoas[x]['idade'] > idadeHomemVelho:
            idadeHomemVelho = pessoas[x]['idade']
            hVelho = pessoas[x]['nome']
print("Analisando informações coletadas", end="")
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
print(f"""A média de idade do grupo é {somaIdade/4:.2f} ano(s).
O homem mais velho é {hVelho.title()}.
Foram informadas {fSub20} mulher(es) com idade abaixo de 20 anos.""")
