animais = ['Cavalo', 'Macaco', 'Calango']
print(f'Lista: {animais}')

#Para adicionar um valor extra a uma lista, usa-se.
animais.append('Pipa')
print(f'Lista adicionando PIPA: {animais}')

#para adicionar valor em lugar específico.
animais.insert(0, 'Cachorro')
print(f'Lista adicionando cachorro no começo: {animais}')

'''Todos os valores contidos na lista são empurrados pra frente'''

'''Para deletar um valor.'''
#del animais[3]
#OU
#animais.pop(3) #animais.pop (remove o último elemento)
#OU
animais.remove('Calango') #Remova a primeira ocorrência
print(f'Lista removendo calango: {animais}')
'''Todos os valores contidos na lista retornam um índice pra trás'''

if 'Macaco' in animais:
    animais.remove('Macaco')
print(f'Lista removendo Macaco: {animais}')

valores = list(range(4, 11))
print(valores)

'''Organização'''
#Ordena por valor.
#valores.sort()
#Ordena por valor ao contrário.
#valores.sort(reverse=True)

#mostra quantidade de índices
#len(valores)

'''valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')
    
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')'''

a = [5, 8, 1, 2]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')


