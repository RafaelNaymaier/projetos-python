#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


lista = list()

while True:
    valor = int(input('Digite um valor: '))

    if valor not in lista:
        lista.append(valor)
        print(f'Valor adicionado com sucesso!')
    else:
        print(f'Valor duplicado! não vou adicionar...')


    encerramento = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if encerramento == 'N':
        lista.sort()
        break

print(f'{lista}')
