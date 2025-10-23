#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#A vista dinheiro/cheque:10% de desconto
#A vista no cartão:5% de desconto
#em até 2x no cartão:Preço normal
#3x ou mais no cartão:20% de juros


print(f'{' LOJAS GUANABARA ':=^40}')

compras = float(input('Preço das compras: R$'))

#Entrada
print('\nFORMAS DE PAGAMENTO')
print('[  1  ] á vista no dinheiro ou cheque')
print('[  2  ] á vista cartão')
print('[  3  ] 2x no cartão')
print('[  4  ] 3x ou mais no cartão')

forma_de_pagamento = int(input('Qual é a opção? '))

#Condições
if forma_de_pagamento == 1:
    print(f'Sua compra de {compras:.2f} vai custar R${compras*0.9:.2f}COM 10% DE DESCONTO')
elif forma_de_pagamento == 2:
    print(f'Sua compra de {compras:.2f} vai custar R${compras*0.95:.2f}COM 5% DE DESCONTO')
elif forma_de_pagamento == 3:
    print(f'Sua compra será parcelada em 2x de R${compras/2:.2f}')
elif forma_de_pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcela}x de R${(compras*1.2)/parcela:.2f} COM JUROS')
    print(f'Sua compra de {compras:.2f} vai custar R${compras*1.20:.2f} no final')
else:
    print('Forma de pagamento inválida. Tente novamente.')










