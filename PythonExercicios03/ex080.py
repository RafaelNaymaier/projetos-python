#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.

#Abre uma lista para variável 'lista'.
lista =  list()

#Diz ao usuário para digitar um número 5 vezes.
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    print(lista)

    #Para cada item na lista, verifica se o valor digitado é menor ou igual, quando encontrado insere o valor digitado pelo usuário na nova posição.
    for cada, item in enumerate(lista):
        if valor <= item:
            lista.insert(cada, valor)
            print(f'Adicionando o valor {valor} na posição {cada}')
            print(lista)
            break

    #Se não encontrado um valor que seja maior que o usuário digitou, valor digitado vai ao final da lista.
    else:
        lista.append(valor)
        print(f'Adicionando o valor {valor} ao final da lista')
        print(lista)

print(lista)













