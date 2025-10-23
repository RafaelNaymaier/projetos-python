import os

def arquivo_existe(nome):
    return os.path.exists(nome)


def cria_arquivo(nome):
    with open(nome, 'w') as arquivo:
        pass


def ler_arquivo(nome_do_arquivo):
    """
    Lê o conteúdo de um arquivo de texto e o retorna.
    :param nome_do_arquivo: O nome do arquivo a ser lido.
    :return: O conteúdo do arquivo como uma string, ou uma string vazia se o arquivo não existir.
    """
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            return conteudo.strip()
    except FileNotFoundError:
        print(f'\033[31mERRO: O arquivo "{nome_do_arquivo}" não foi encontrado.\033[m')
        return ''


def cadastrar_pessoa(nome_do_arquivo):
    nome = str(input('Nome: ')).strip()
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido para a idade.\033[m')

    with open(nome_do_arquivo, 'a') as arquivo:
        arquivo.write(f'{nome:<30}{idade:>3} anos\n')
        print(f'A pessoa {nome} foi cadastrada com sucesso.')






