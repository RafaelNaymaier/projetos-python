#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = 2018 - ano_nascimento

pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salario: R$'))
    pessoa['aposentadoria'] = 35 -(2018 - pessoa['contratação']) + pessoa['idade']

print (f'{'='*30}')

for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}.')


























