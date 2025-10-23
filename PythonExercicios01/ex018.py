#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import cos, sin, tan, radians
ângulo = float(input('Digite o ângulo que você deseja'))

rad = radians(ângulo)

print ('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, sin(rad)))
print ('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo,cos(rad)))
print ('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo,tan(rad)))
