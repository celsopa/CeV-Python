# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Arredondar', 'Bissetriz', 'Constituinte', 'Delegado',
            'Elefante', 'Felicidade', 'Geladeira', 'Idiota')
vogais = 'a', 'e', 'i', 'o', 'u'

for p in palavras:
    print(f'{p}: {list(filter(lambda x: x in vogais, p.lower()))}')