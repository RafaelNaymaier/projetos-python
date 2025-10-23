#Crie um programa que leia um número real qualquer pelo teclado e mostra na tela a sua porção inteira
#Ex: digite um número:6.127               O número 6.127 tem a parte inteira 6                math

#Formas diferentes de resolver o mesmo problema

#Forma 1
#from math import trunc
#valor = float(input('Digite um valor: '))
#inteira = trunc(valor)

#print ('O valor digitado foi {:.3f} e a sua porção inteira é {}'.format(valor, inteira))

#Forma 2
#import math
#valor = float(input('Digite um valor: '))
#inteira = math.trunc(valor)

#print ('O valor digitado foi {:.3f} e a sua porção inteira é {}'.format(valor, inteira))

#Forma 3
#valor = float(input('Digite um valor: '))

#print ('O valor digitado foi {:.3f} e a sua porção inteira é {:.0f}'.format(valor, valor // 1))

#Forma 4
import math
valor = float(input('Digite um valor'))

print ('O valor digitado foi {:.3f} e a sua porção inteira é {}'.format(valor, math.trunc(valor)))



