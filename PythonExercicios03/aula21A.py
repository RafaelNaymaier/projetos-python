'''help(input)'''
'''DOCSTRINGS'''


def contador (i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :Param i: Inicio da contagem
    :Param f: Fim da contagem
    :Param p: Passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')




#Função com parâmetros opcionais
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2)

somar(c=3, a=2)

"""ESCOPO DE VARIÁVEIS"""

"""x == variável local"""
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa principal
"""n == variável global"""
n = 2
print(f'No programa principal, n vale {2}')
teste()

def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}')

n1 = 2
funcao()
print(f'n1 global vale {n1}')


#Transformando variável local em global
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


"""RETORNO DE VALORES"""


"""Return pode entregar um resultado a uma variável"""
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = (2, 2)
r3 = 6

print(f'Meus cálculos deram {r1}, {r2} e {r3}')


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados foram {f1}, {f2}, {f3}')


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a fatorial de {fatorial(n)}')

def par(n = 0):
    if n%2==0:
        return True
    else:
        return False


num = int(input('Digite um número'))
if par(num):
    print('é par')
else:
    print('Não é par')







