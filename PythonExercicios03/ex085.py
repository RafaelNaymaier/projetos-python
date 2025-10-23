#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

lista_numeros = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista_numeros[1].append(valor)
    else:
        lista_numeros[0].append(valor)

lista_numeros[1].sort()
lista_numeros[0].sort()

print(f'Os valores pares digitados foram: {lista_numeros[1]}')
print(f'Os valores ímpares digitados foram: {lista_numeros[0]}')


























