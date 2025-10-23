#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
#Média > 7: aprovado

situacao = dict()
aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print(aluno)

for chave, valor in aluno.items():
    print(f'{chave} é igual a {valor}')


















