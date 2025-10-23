#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
#80000
#10000
#7

valor = float(input('Valor: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = valor / (12 * anos)

print ('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} '.format(valor,anos,prestação))

if salário *0.3 >= prestação:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print ('Empréstimo NEGADO!')























