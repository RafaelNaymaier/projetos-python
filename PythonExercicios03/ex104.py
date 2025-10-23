#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
#só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

#Função que lê se um número é inteiro.
def leiaint(msg):
    #Loop de validação
    while True:
        try:
            msg = int(input('Digite um número'))
            return msg
        except ValueError:
            print('ERRO! Digite um número inteiro válido')


#Programa principal
numero = leiaint('Digite um número')
print(f'Você acabou de digitar o número {numero}')