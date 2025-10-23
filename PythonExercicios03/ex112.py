#Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
#Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.



from uteis import moeda
from uteis import dados

valor = dados.leiadinheiro('Digite o preço: R$')

moeda.resumo(valor, 35, 22)


#print(valor)






