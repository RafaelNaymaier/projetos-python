nome = input ('Digite seu nome: ') # poderia ser 'str(input ('Digite seu nome:)'
print ('Prazer em te conhecer {:20}!'.format(nome)) # {:20} 20=espaços
print ('Prazer em te conhecer {:20}!'.format(nome)) # {:>20} 20=espaços, alinhamento a direita
print ('Prazer em te conhecer {:20}!'.format(nome)) # {:^20} 20=espaços, centralizado
print ('Prazer em te conhecer {:20}!'.format(nome)) # {:=^20} 20=espaços, centralizado, '=' em volta

n1 = int(input ('Um valor'))
n2 = int(input ('Outro valor'))
print ('A soma vale {}'.format(n1+n2))

n1 = int(input ('Um valor'))
n2 = int(input ('Outro valor'))
s = n1+n2 #soma
m = n1*n2 #multiplicação
d = n1/n2 #divisão
di = n1//n2 #divisão inteira
e = n1**n2 #exponenciação
print ('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d)) # caso queira com 2 casas ={:.3f}
print ('Divisão inteira {} e potência {}'.format(di, e))


