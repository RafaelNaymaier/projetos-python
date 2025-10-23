#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

vezes = 0
lista = list()

#Loop principal
while True:
    lista.append(int(input('Digite um valor: ')))
    vezes += 1
    encerramento = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    #Encerra o programa
    if encerramento in 'nN':
        lista.sort(reverse=True)
        break


print(f'Você digitou {vezes} elementos.')
print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista')

























