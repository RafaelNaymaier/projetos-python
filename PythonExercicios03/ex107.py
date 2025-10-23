#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.









from uteis import numeros

preco = int(input('Digite o preço: R$'))

print(f'A metade de {numeros.metade(preco)}')
print(f'O dobro de {preco} é {numeros.dobro(preco)}')
print(f'Aumentando 10% temos {numeros.aumento_porcentagem(preco, 10)}')




























