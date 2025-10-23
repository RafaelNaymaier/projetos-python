#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$ 1000.
#C) qual é o nome do produto mais barato.

print(f'{'-'*30} \n{'LOJA SUPER BARATÃO'.center(30)} \n{'-'*30}')

total = produto_caro = contagem = 0

#Loop principal
while True:
    nome_produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    contagem += 1
    total += preco

    #Dá valor a variáveis no primeiro input do usuário.
    if contagem == 1:
        produto_barato = preco
        nome_produto_barato = nome_produto

    #Verifica qual é o produto mais barato.
    if preco < produto_barato:
        produto_barato = preco
        nome_produto_barato = nome_produto

    #Verifica produtos acima de R$ 1000
    if preco > 1000:
        produto_caro += 1

    encerramento = ' '
    #Valida o encerramento do programa
    while encerramento not in 'SN':
        encerramento = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if encerramento == 'N':
        print(f'{'-'*15} FIM DO PROGRAMA {'-'*15}')
        break

#Informa os resultados
print(f'O total da compra foi R$ {total}')
print(f'Temos {produto_caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome_produto_barato} que custa R$ {produto_barato}')










