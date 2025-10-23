#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintala.
#sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Largura da sua parede'))
altura = float(input('Altura da sua parede'))
área = largura*altura

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m²'.format(largura,altura, área))
print ('Para pintar essa parece, você precisará de {}l de tinta.'.format(área/2))