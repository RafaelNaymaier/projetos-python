#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9anos:MIRIM
#Até 14 anos:INFANTIL
#Até 19 anos :JUNIOR
#até 25 anos :SÊNIOR
#Acima: Master

#from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = 2017 #Se fosse para puxar o ano atual do computador ---> #date.today().year
idade = ano_atual - ano_nascimento

print(f'O atlteta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')












