


def fatorial(num):
    f = 1
    for c in range(1, num+1):
        f *= c
    return f


def metade(num, formatado=False):
    if formatado:
        return moeda(num / 2)
    return num / 2


def dobro (num, formatado=False):
    if formatado:
        return moeda(num * 2)
    return num* 2


def triplo (num, formatado=False):
    if formatado:
        return moeda(num * 3)
    return num * 3



def aumento_porcentagem(num, porcentagem, formatado=False):
    if formatado:
        return moeda(num + (num * porcentagem/100))
    return num + (num * porcentagem/100)



def diminui_porcentagem(num, porcentagem, formatado=False):
    if formatado:
        return moeda(num - (num * porcentagem/100))
    return num - (num * porcentagem/100)



def moeda(num):
    return f'R$ {num:.2f}'.replace('.', ',')



def resumo(num,aumento=10,diminui=5):
    print('-'*30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-'*30)
    print(f'Preço analisado:  {moeda(num)}')
    print(f'Dobro do preço:   {dobro(num, True)}')
    print(f'Metade do preço:  {metade(num, True)}')
    print(f'{aumento}% de aumento:   {aumento_porcentagem(num, aumento, True)}')
    print(f'{diminui}% de redução:   {diminui_porcentagem(num, diminui, True)}')
    print('-'*30)









