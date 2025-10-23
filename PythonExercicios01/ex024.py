#Crie um programa que leia o nome de uma pessoa e diga se ela começa ou não com o nome "SANTO"
#Mario da Silva Mendonça


#cidade = str(input('Qual é seu nome completo? ')).strip().lower()

#print (cidade.startswith('santo'))

cidade = str(input('Qual é seu nome completo? ')).strip().lower()

#print (cidade.find('silva')>=0)

print('seu nome tem Silva? {} '.format('silva' in cidade))