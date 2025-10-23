#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar.
#Se é a hora de se alistar.
#Se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = datetime.today().year
idade = ano_atual - ano_nasc
ano_alistamento = ano_nasc + 18

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc,idade, ano_atual))

if idade < 18:
    faltam = 18 - idade
    print('Aínda faltam {} anos para o alistamento'.format(faltam))
    print('Seu alistamento será em {}.'.format(ano_alistamento))

elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade > 18:
    passou = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(passou))
    print('Seu alistamento foi em {}.'.format(ano_alistamento))

#print(idadeatual)




