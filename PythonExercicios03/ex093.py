#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#Inicia as variáveis
jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome: '))

numero_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(1, numero_partidas+1):
    gols.append(int(input(f'Quantos gols na partida {p}?')))

#Copia a lista 'gols' para o dicionário 'jogador'
jogador['gols'] = gols.copy()

#Faz a soma de todos os valores dentro de 'gols' para dentro do dicionário
jogador['total'] = sum(gols)

print(f'{'='*30}\n{jogador}\n{'='*30}')

#Para valor dentro de chave.
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print(f'{'='*30}')

print(f'O jogador {jogador["nome"]} jogou {numero_partidas} partidas.')

#Para gol dentro de partida
for p, g in enumerate(gols):
    print(f'Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')









