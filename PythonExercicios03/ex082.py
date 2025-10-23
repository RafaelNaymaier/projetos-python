#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

lista_numeros = list()
lista_pares = list()
lista_impares = list()

while True:
    lista_numeros.append(int(input('Digite um valor: ')))
    encerramento = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if encerramento in 'nN':
        break

for i, valor in enumerate(lista_numeros):
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)


print(f'A lista completa é {lista_numeros}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')


















