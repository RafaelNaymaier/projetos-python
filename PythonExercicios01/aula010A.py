#Condições simples e compostas

#carro.siga() #'carro' é objeto                   '.siga' é o método


#Estrutura condicional


#Condição simplificada

tempo = int(input('Quantos anos tem carro? '))
print('Carro novo' if tempo<=3 else 'Carro velho')
print('--FIM--')

nome = input('Digite seu nome: ')
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print ('Seu nome é tão normal')

print('Bom dia, {}'.format(nome))

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
m = (n1 + n2) / 2
print ('aA sua média foi {:.1f}'.format(m))
print('Parabéns' if m>=6 else 'Estudo mais')

#Condição composta

if m >= 6.0:
    print('Sua média foi boa! PARABÉNS! ')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

    tempo = int(input('Quantos anos tem carro? '))

    if tempo <= 3:
        True
        print('Carro novo')
    else:
        False
        print('Carro velho')

    print('--FIM--')



