#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

menor = n1 #atribui n1 a menor
if n2 < menor : menor = n2 #se n2 for < do que menor então menor = n2
if n3 < menor : menor = n3

maior = n1
if n2 > maior : maior = n2
if n3 > maior : maior = n3

print('O menor valor digitado foi {}'.format(menor))
print ('O maior valor digitado foi {}'.format(maior))


