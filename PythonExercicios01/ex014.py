#Escreva um programa que converta uma temperatura digitada em ºc e converta para ºf

celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = (celsius * 1.8) + 32

print ('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(celsius, fahrenheit))