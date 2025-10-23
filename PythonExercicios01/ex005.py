#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

n1 =int(input ('Digite um valor'))
ant = n1-1
suc =  n1+1

#caso precise guardar as variáveis
print ('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n1, ant ,suc))

#caso não precise guardar as variáveis
#print ('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n1, n1-1, n1+1))