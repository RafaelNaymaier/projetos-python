#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


'''def voto(ano_nascimento):
    idade = 2018 - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade <= 17 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO '



nascimento = int(input('Digite o ano de nascimento: '))

print(f'{voto(nascimento)}')'''


def voto(idade_funcao):
    if idade_funcao < 16:
        return f'NÃO VOTA'
    elif 16 <= idade_funcao <= 17 or idade_funcao > 65:
        return f'VOTO OPCIONAL'
    else:
        return f'VOTO OBRIGATÓRIO '



nascimento = int(input('Digite o ano de nascimento: '))
idade = 2018 - nascimento

print(f'Com {idade} anos: {voto(idade)}')




















