#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

'''for c in range (1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior: #ignorar o sublinhado
        maior = peso
    if peso < menor: #ignorar o sublinhado
        menor = peso

print(f'\nO maior peso lido foi de {maior}kg')
print(f'\nO menor peso lido foi de {menor}kg')'''



peso = float(input('Peso da 1ª pessoa: '))

maior = peso
menor = peso

for c in range (2, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso

print(f'\nO maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')














