def linha(tamanho):
    print('-'*tamanho)



def titulo(msg, tamanho):
    print('-'*tamanho)
    print(f'{msg:^30}')
    print('-'*tamanho)


def cabecalho(msg, tamanho, lista):
    """
    Cria um interface com opções numeradas baseados nos elementos da lista
    :param lista: para cada opção dentro de lista, é criado um número e uma linha para organização do interface.
    :param msg: Texto da mensagem
    :param tamanho: tamanho da linha e do título
    """
    titulo(msg, tamanho)
    for i, opcao in enumerate(lista):
        print(f'\033[33m{i + 1}\033[m - \033[34m{opcao}\033[m')
    linha(tamanho)



































