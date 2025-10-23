#Faça um programa que leia um número qualquer e mostre o seu fatorial
#Ex 5! = 5x4x3x2x1 = 120



num= int(input('Digite um número para calcular o seu fatorial'))

resultado = 1 #Guarda resultado

print(f'Calculando {num}! =', end=' ')

while num > 0:
    resultado *= num
    print(f'{num}', end=' ')
    print(' x ' if num > 1 else ' = ', end=' ')
    num -= 1

print(f'{resultado}')

















