#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.




def ficha(nome_jogador='', jogador_gols=''):
    if not nome_jogador:
        nome_jogador = '<desconhecido>'
    if not jogador_gols.isnumeric():
        jogador_gols = 0
    else:
        jogador_gols = int(jogador_gols)
    return f'O jogador {nome_jogador} fez {jogador_gols} gol(s) no campeonato.'




#Programa
print('-'*30)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))



print(ficha(nome, gols))

















