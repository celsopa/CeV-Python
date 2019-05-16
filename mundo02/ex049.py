# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input("Informe um valor para ver sua tabuada de multiplicação: "))
print(f"""A tabuada de multiplicação de {n} é:
{'-'*12}""")
for x in range(1, 11):
    print(f"{n} x {x:>2} = {n*x:>3}")
print(f"{'-'*12}")