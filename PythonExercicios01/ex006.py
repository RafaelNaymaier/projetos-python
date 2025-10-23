#Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raíz quadrada

n1 = int(input ('Digite um número'))
d = n1*2
t = n1*3
r = n1**(1/2)

#caso precise guardar as variáveis
#print ('O dobro de 85 vale {} \n O triplo de 85 vale {} \n A raíz quadrada de 85 é igual a {:.2f}'.format(d, t, r))

#caso não precise guardar as variáveis
#print ('O dobro de 85 vale {} \n O triplo de 85 vale {} \n A raíz quadrada de 85 é igual a {:.2f}'.format(n1*2, n1*3, n1**(1/2)))

#raíz quadrada com raíz quadrada usando "pow"
print ('O dobro de 85 vale {} \n O triplo de 85 vale {} \n A raíz quadrada de 85 é igual a {:.2f}'.format(n1*2, n1*3, pow(n1, (1/2))))