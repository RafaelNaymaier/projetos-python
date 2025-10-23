#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero:Todos os lados iguais
#Isósceles:dois lados iguais
#Escaleno:todos os lados diferentes


lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))

classificacao = ''

# Verificar se não forma triângulo
if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <=lado1:
    print('Os segmentos NÃO PODEM FORMAR um triângulo')

# Determinar classificação
elif lado1 == lado2 == lado3:
    classificacao = 'EQUILÁTERO'
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    classificacao = 'ISÓSCELES'
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    classificacao = 'ESCALENO'

#Se classificacao tiver algo
if classificacao:
    print (f'Os segmentos acima PODEM FORMAR um triângulo {classificacao}')









