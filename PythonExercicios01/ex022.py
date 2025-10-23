#crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

#nome = input('Digite seu nome completo:')

#rep = nome .replace(' ','')[1:]

#pnome = nome.split()[0]

#pnomenum = pnome.count('')


#test = nome.count('')-nome.count(' ')

#print('Seu nome em maiúsculas é {}'.format(nome.upper()))
#print('Seu nome em minúsculas é {}'.format(nome.lower()))
#print('Seu nome tem ao todo {} letras'.format(rep.count('')))
#print('Seu primeiro nome é {} e ele tem {} letras '.format(pnome,pnomenum-1))

nome = input('Digite seu nome completo: ')

a = len(nome) - nome.count(' ')
b = nome.split()[0]
c = len(b)

print ('Seu nome em maiúsculas é {}'.format(nome.upper()))
print ('Seu nome em minúsculas é {}'.format(nome.lower()))
print ('Seu nome tem ao todo {} letras'.format(a))
print ('Seu primeiro nome é {} e ele tem {}'.format(b,c))


