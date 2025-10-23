#Exercício Python 096: Faça um programa que tenha uma função chamada área()
#que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#Função titulo
def titulo(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

#Função area
def area(largura_area, comprimento_area):
    area1 = largura_area * comprimento_area
    print(f'A área de um terreno {largura_area}x{comprimento_area} é de {area1}m².')


titulo('Controle de terrenos')

largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))

area(largura_area=largura, comprimento_area=comprimento)













