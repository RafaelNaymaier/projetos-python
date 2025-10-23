#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de para.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando flag)

soma = vezes = 0

while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    vezes += 1

print(f'A soma dos {vezes} valores foi {soma}!')

























