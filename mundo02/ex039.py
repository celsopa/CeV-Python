# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Informe o ano de seu nascimento: '))
atual = date.today().year
print(f"Quem nasceu em {nasc} completa {atual-nasc} ano{'' if atual-nasc==1 else 's'} em {atual}.")
if atual - nasc> 18:
    print(f"Já passou da época do seu alistamento militar.\nVocê está atrasado em {atual-nasc-18} ano{'' if atual-nasc-18==1 else 's'}!")
elif atual - nasc < 18:
    print(f"Falta{'' if 18-(atual-nasc)==1 else 'm'} {18-(atual-nasc)} ano{'' if 18-(atual-nasc)==1 else 's'} para o seu alistamento militar.")
else:
    print("PARABÉNS!!!! Esse é o ano do seu serviço militar!")