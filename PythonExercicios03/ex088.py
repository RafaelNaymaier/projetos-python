#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


#Importa funções de bibliotecas
from random import randint
from time import sleep

#Cabeçalho do programa
print(f'{'-'*30}\n{'JOGA NA MEGA SENA'.center(30)}\n{'-'*30}')

lista_numeros = []

quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

#Loop principal repetindo quantas vezes o usuário escolheu.
for j in range(1, quantidade_jogos+1):

    #Loop para gerar 6 números diferentes
    while len(lista_numeros) <6:
        numero_gerado = (randint(0, 60))

        #Verificação se número já existe na lista 'numeros_sorteados'
        if numero_gerado not in lista_numeros:
            lista_numeros.append(numero_gerado)

    #Organiza a lista após gerar 6 números diferentes
    lista_numeros.sort()

    #Imprime na tela os resultados
    print(f'Jogo {j}: {lista_numeros}')

    #Organiza os valores em ordem crescente.
    lista_numeros.clear()

    #Timer de 0.5 segundos
    sleep(0.5)

print(f'{'-'*10} {'< BOA SORTE! >'} {'-'*10}')
