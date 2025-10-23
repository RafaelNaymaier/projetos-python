#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


#Inicia as variáveis
jogadores = list()
gols = list()

#Loop principal
while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome: '))
    numero_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, numero_partidas+1):
        gols.append(int(input(f'Quantos gols na partida {p}?')))

    #Copia gols por partida e o total para jogador, depois apaga 'gols'
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    #Copia o dicionário 'jogador' para a lista de 'jogadores'
    jogadores.append(jogador.copy())

    encerramento = str(input('Deseja continuar? [S/N] '))
    if encerramento in 'Nn':
        break

#Para valor dentro de chave.
print(f'{'='*30}')
print(f'{'cod':<3} {'nome':<15} {'gols':<15} {'total':<10} \n{'-'*30}')

for n, j in enumerate(jogadores):
    print(f'{n:>3} {j["nome"]:<15} {str(j["gols"]):<15} {j["total"]:<10}')
print(f'{'-'*30}')

while True:
    seletor = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if seletor == '999':
        break
    if seletor <= len(jogadores)-1:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[seletor]["nome"]}:')
        for p, gols_na_partida in enumerate(jogadores[seletor]['gols']):
            print(f'Na jogo {p + 1}, fez {gols_na_partida} gols.')
        print(f'{'-'*30}')
    else:
        print('O jogador nao existe!')




