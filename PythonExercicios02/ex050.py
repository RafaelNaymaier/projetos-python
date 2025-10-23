#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o


soma = 0
contagem = 0

for c in range(1, 7):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 ==0:
        soma += valor
        contagem += 1

print(f'Você informou {contagem} números pares e a soma foi {soma}')



















