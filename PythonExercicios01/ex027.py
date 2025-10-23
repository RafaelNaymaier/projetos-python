#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex:Ana Maria de Souza
#Primeiro = Ana
#Segundo = Souza


nome = str(input('Digite seu nome completo: ')).strip().split()


#print (nome[0])
#print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))

print('Seu último nome é {}'.format(nome[len(nome)-1]))

#Formas de resolver o mesmo problema

#Forma 01
"""nome = str(input('Digite seu nome completo: '))

a = len(nome) - nome.count(' ')
b = nome.split()[0]
c = len(b)

print ('Analisando seu nome...')
print ('Seu nome em maiúsculas é {}'.format(nome.upper()))
print ('Seu nome em minúsculas é {}'.format(nome.lower()))
print ('Seu nome tem ao todo {} letras'.format(a))
print ('Seu primeiro nome é {} e ele tem {} letras'.format(b,c))

#Forma 02

nome = str(input('Digite seu nome completo: ')).strip()
print ('Analisando seu nome...')
print ('Seu nome em maiúsculas é {}'.format(nome.upper()))
print ('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

#print ('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

separa = nome.split() #está separando o nome em listas
print ('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))'''
