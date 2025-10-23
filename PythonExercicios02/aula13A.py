Estrutura de repetição com variável de controle

Laços
Repetições
Iterações


for c in range(1, 10): #, -1): conta ao contrário # (1, 10, 2): conta de 1 a 10 pulando de 2 em 2
    #Pode ser usado if antes do que vai ser repetidido para verificar variáveis.
        #O que vai ser usado após o if.
    #O que vai ser repetido de 1 a 10 vezes.
#O que vai ser feito após a repetição.

    n = int(input('Digite um número: '))
    for c in range(0, n + 1):
        print(c)
    print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')


s = 0
for c in range (0, 4):
    n = int(input('Digite um valor inteiro: '))
    s += n
print(f'O somatório de todos os valores foi {s}')






