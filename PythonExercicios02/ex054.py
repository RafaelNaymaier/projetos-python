#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas aínda não atingiram a maioridade e quantas já são maiores.

maior = 0
menor = 0

for c in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if 2017 - ano_nasc <= 21:
        menor += 1
    else:
        maior += 1
print()

print(f'Ao todo tivemos {maior} pessoas maiores de idade'
      f'\nE também tivemos {menor} pessoas menores de idade')























