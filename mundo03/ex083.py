# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
# na ordem correta.

expressao = input('Digite sua expressão: ')
pAbre = 0
for x in expressao:
    if x == "(":
        pAbre += 1
    elif x == ")":
        pAbre -= 1
    if pAbre == -1:
        print('Expressão inválida!')
        break
if pAbre == 0:
    print('Sua expressão é válida!')
