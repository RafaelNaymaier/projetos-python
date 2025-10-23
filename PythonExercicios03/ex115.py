#Exercício Python 115ª: Vamos criar um interface em Python, usando modularização.
from uteis import pastas
from uteis import interface

cadastro = 'pessoas_cadastradas.txt'

lista_menu = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']

while True:
    try:
        interface.cabecalho('MENU PRINCIPAL', 30, lista_menu)
        opcao = int(input(f'\033[33mSua opção\033[m: '))
    except ValueError:
        print('\033[31mERRO! por favor, digite um número inteiro válido\033[m')
        continue # Retorna ao início do loop
    except KeyboardInterrupt:
        print('\n\033[31mO usuário preferiu sair do sistema.\033[m')
        break

    if opcao == 1:
        if not pastas.arquivo_existe(cadastro):
            interface.titulo('NÃO HÁ PESSOAS CADASTRADAS', 30)
            pastas.cria_arquivo(cadastro)
        else:
            interface.titulo('PESSOAS CADASTRADAS', 30)
            print(pastas.ler_arquivo(cadastro))

    elif opcao == 2:
        interface.titulo('NOVO CADASTRO', 30)
        pastas.cadastrar_pessoa(cadastro)

    elif opcao == 3:
        interface.titulo('Saíndo do sistema... Até logo!', 30)
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida!\033[m')
