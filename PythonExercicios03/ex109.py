#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


from uteis import numeros

valor = float(input('Digite um valor: '))

print(f'A metade de {numeros.moeda(valor)} é {numeros.metade(valor, True)}')
print(f'O triplo de {numeros.moeda(valor)} é {numeros.triplo(valor, True)}')
print(f'Aumentando 10% temos {numeros.aumento_porcentagem(valor, 10, True)}')
print(f'Reduzindo 10% temos {numeros.diminui_porcentagem(valor, 10, True)} ')






























