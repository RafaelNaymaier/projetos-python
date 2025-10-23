#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

#from math import sqrt
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

#print ('A hipotenusa vai medir {:.2f}'.format(sqrt(oposto*oposto+adjacente*adjacente)))

from math import hypot
print ('A hipotenusa vai medir {:.2f}'.format(hypot(oposto, adjacente)))