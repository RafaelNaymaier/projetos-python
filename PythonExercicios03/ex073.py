#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.


times_brasileirao = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 'Mirassol', 'São Paulo', 'Bragantino', 'Fluminense', 'Internacional', 'Ceará SC', 'Corinthians', 'Grêmio', 'Atlético-MG', 'Vasco da Gama', 'Santos', 'EC Vitória', 'Juventude', 'Fortaleza', 'Sport', 'Recife')

#Mostra a lista de times.
print(f'{'='*30} \nListas de time do Brasileirão: {times_brasileirao} \n{'='*30}')

#Mostra os 5 primeiros times
print(f'Os 5 primeiros são: {times_brasileirao[0:5]} \n{'='*30}')

#Mostra os 4 últimos colocados.
print(f'Os 4 últimos são: {times_brasileirao[-4:]} \n{'='*30}')

#Mostra os times em ordem alfabética.
print(f'Times em ordem alfabética: {sorted(times_brasileirao)} \n{'='*30}')

#Mostra posição do internacional
print(f'O Internacional está na {times_brasileirao.index('Internacional')+1}ª posição')


