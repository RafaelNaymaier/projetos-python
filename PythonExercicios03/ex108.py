#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


from uteis import numeros

preco = int(input('Digite o preço: R$'))



print(f'A metade de {preco} é {numeros.moeda(numeros.metade(preco))}')
print(f'O dobro de {preco} é {numeros.moeda(numeros.dobro(preco))}')
print(f'Aumentando 10% temos {numeros.moeda(numeros.aumento_porcentagem(preco, 10))}')












