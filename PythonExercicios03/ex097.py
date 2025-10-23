#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#Ex:escreva(‘Olá, Mundo!’)

def escreva(msg):
    print(f'{'~'*(len(msg)+4)}')
    print(f'  {msg}  ')
    print(f'{'~'*(len(msg)+4)}')


escreva('Curso de python no youtube')









