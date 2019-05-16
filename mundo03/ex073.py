# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Santos', 'São Paulo', 'Atlético-MG', 'Botafogo', 'Athlético-PR', 'Flamengo', 'Bahia',
'Internacional', 'Goiás', 'Cruzeiro', 'Corinthians', 'Chapecoense', 'Ceará-SC', 'Fluminense', 'Fortaleza',
'CSA', 'Grêmio', 'Avaí', 'Vasco da Gama')

print(f'Lista de times do Campeonato Brasileiro: {times}')
print()
print('Os cinco PRIMEIROS colocados')
for i in range(5):
    print(f'{i+1}º - {times[i]}')
print()
print('Os cinco ÚLTIMOS colocados')
for i in range(len(times)-1, len(times)-5, -1):
    print(f'{i+1}º - {times[i]}')
print()
print(f'Times em ordem Afabética: {sorted(times)}')
print()
print(f'O time Chapecoense está na {times.index("Chapecoense")+1}ª posição')