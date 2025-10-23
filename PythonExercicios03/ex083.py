#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = list()
correto = True

expressao = input('Digite sua expressão: ')

for indice in expressao:
    if indice == '(':
        lista.append('(')

    elif indice == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            correto = False
            break

if correto and len(lista) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')




















