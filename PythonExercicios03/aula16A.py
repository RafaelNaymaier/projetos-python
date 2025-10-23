lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#Tuplas são imutáveis

'''#Simples
for comida in lanche:
    print(f'Eu vou comer {comida}')

#Se precisar de posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#Se precisar de posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''

#Não altera, apenas coloca em ordem alfabética.
'''print(sorted(lanche))'''

#Junta as duas tuplas, formando a tupla 'c'
'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b'''

#Quantas vezes 5 aparece na tupla 'c'
'''print(c.count(5))'''

#Em que posição está o 8 (Apenas a primeira ocorrência)
'''print(c.index(8))'''

#Onde começar a contagem (Conhecido como 'DESLOCAMENTO')
'''print(c.index(8, 1))'''

#Para armazenar
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

#Para apagar tupla
'''del(pessoa)'''






