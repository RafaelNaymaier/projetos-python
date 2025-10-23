#Crie um programa que leia dois valores e mostre um interface na tela
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] saír do programa
#Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep

primeiro_valor = int(input('Informe o primeiro valor: '))
segundo_valor = int(input('Informe o segundo valor: '))

fim = False
while not fim:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair')
    while True:
        try:
            opcao = int(input('>>>>>>>>> Qual é a sua opção?'))
            break
        except ValueError:
            print('Opção inválida. Tente novamente.')
    if opcao == 1: #Soma
        print(f'A soma entre {primeiro_valor} + {segundo_valor} é {primeiro_valor + segundo_valor}')
    elif opcao == 2:
        print(f'O resultado de {primeiro_valor} x {segundo_valor} é {primeiro_valor * segundo_valor}')
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior é {primeiro_valor}')
        else:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior é {segundo_valor}')
    elif opcao == 4:
        while True:
            try:
                primeiro_valor = int(input('Informe o primeiro valor: '))
                segundo_valor = int(input('Informe o segundo valor: '))
                break
            except ValueError:
                print('Opção inválida. Tente novamente.')
    elif opcao == 5:  # Finaliza o programa
            print('Finalizando...')
            fim = True
    else:
        print('Opção inválida. Tente novamente.')
    print('=' * 30)
    sleep(2)
print('Fim do programa! Volte sempre!')















