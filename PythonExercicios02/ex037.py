#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

''''{:b} → Binário (ex: 1010)
{:o} → Octal (ex: 12)
{:d} → Decimal (padrão)
{:x} → Hexadecimal minúsculo
{:X} → Hexadecimal maiúsculo'''

numero = int(input('Digite um número inteiro: '))
print ('[ 1 ] converter para BINÁRIO')
print ('[ 2 ] converter para OCTAL')
print ('[ 3 ] converter para HEXADECIMAL')
opçao = int(input('Sua opção: '))

if opçao == 1:
    print('{} convertido para BINÁRIO é igual a {:b}'.format(numero, numero)) # poderia ser bin(num)[2:]
elif opçao ==2:
    print('{} convertido para OCTAL é igual a {:o}'.format(numero,numero))
elif opçao ==3:
    print('{} convertido para HEXADECIMAL é igual a {:x}'.format(numero,numero))
else:
    print('Opção inválida, tente novamente.')















