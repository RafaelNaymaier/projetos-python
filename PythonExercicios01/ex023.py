#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: Digite um número :1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1


'''A divisão inteira por 1000 pega apenas o dígito do milhar pq descarta a parte decimal e retorna apenas a parte inteira da divisão'''

#cálculo para divisão real = 100//100  = 1           pois 100 cabe 1 vez dentro de 100                            OU 100/100 = 1
#cálculo para resto de divisão 23%10 =  3   é o resultado pois é o resto da divisão, 23/10 = 2.3  porém 2 é ignorado pois é real

#Formas de resolver o mesmo problema

#Forma 01
num = int(input('Informe um número: '))

numm = num// 1000 % 10 #quantas vezes 1000 cabe inteiramente em num, sobra é ignorada
numc = num // 100 % 10 #pega o resto de divisão '%" e divide por num (1234) 1234 - 1000, a sobra é o resultado do resto de divisão (123). divisão inteira de : 234 // 100 = 2, pois cabe 2 vezes o valor 100 dentro de 234
numd = num // 10 % 10 #numd = num%100//10
numu = num // 10  % 10 # (23 / 10) = 2 portanto 23 % 10 = 3


print ('Analisando o número {}'.format(num))
print ('Unidade : {}'.format(numu))
print('Dezena: {}'.format(numd))
print ('Centena: {}'.format(numc))
print('Milhar: {}'.format(numm))

#Forma 02 Porém só mostra o resultado certo caso tenha 4 valores

#num = int(input('Informe um número: '))
#n = str(num)

#print('Analisando o número {}'.format(n))
#print ('Unidade: {}'.format(n[3]))
#print ('Dezena: {}'.format(n[2]))
#print ('Centena: {}'.format(n[1]))
#print ('Milhar: {}'.format(n[0]))







