#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'

'''for c in palavras:
    print(f'Na palavra {c} temos as vogais ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra.lower(), end= ' ')
    print()'''

for c in palavras:
    print(f'Na palavra {c} temos as vogais ', end= '')
    for letra in c:
        if letra in 'AEIOU':
            print(letra.lower(), end= ' ')
    print()

























