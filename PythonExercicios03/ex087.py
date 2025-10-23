#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = soma_terceira_coluna = maior_segunda_linha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        #Soma dos valores pares
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        #Soma dos valores da terceira coluna
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]
        #Maior valor da segunda linha
        if linha == 1:
            if coluna == 0:
                maior_segunda_linha = matriz[linha][coluna]
            elif matriz[linha][coluna] > maior_segunda_linha:
                maior_segunda_linha = matriz[linha][coluna]

print(f'{'*'*30}')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'{'*'*30}')

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')

















