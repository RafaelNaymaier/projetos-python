#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print(f'{'='*30}\n {'Listagem de preço'.center(30)} \n{'='*30}')

'''#'Palavra' = string
produtos = 'Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro'
#sem aspas = int ou float
preco = 1.72, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90

#Zip percorre até a variável com a coleção mais curta.
for produto, preco in zip(produtos, preco):
    print(f'{produto:.<20}R${preco:>7.2f}')'''

'''# Agora a variável 'produtos' é uma tupla que contém outras tuplas.
# Cada tupla interna guarda o nome e o preço de um produto.
produtos = (
    ('Lápis', 1.72),
    ('Borracha', 2.00),
    ('Caderno', 15.90),
    ('Estojo', 25.00),
    ('Transferidor', 4.20),
    ('Compasso', 9.99),
    ('Mochila', 120.32),
    ('Canetas', 22.30),
    ('Livro', 34.90))

for item in produtos:
    print(f'{item[0]:.<20}R${item[1]:>7.2f}')'''

produtos = 'Lápis', 1.72, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<20}R$ {produtos[c+1]:>6.2f}')


















