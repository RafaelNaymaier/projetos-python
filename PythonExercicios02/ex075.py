#Exercício Python 075:
#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


numero = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: '))

print(f'{'='*30}\nVocê digitou os valores: {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')

if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram', end=' ')
for p in numero:
    if p % 2 == 0:
        print(f'{p}', end=' ')
