#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

lista_pessoas = list()
soma = 0

#Loop principal
while True:
    dados = dict()

    #Coleta de dados E Validação
    while True:
        dados['nome'] = str(input('Nome: ')).strip()
        if dados['nome'] and dados['nome'].replace(' ', '').isalpha():
            break
        print(f'ERRO! Apenas letras')

    #Validação
    while True:
            dados['sexo'] = str(input('sexo: [F/M]: ')).upper()
            if dados['sexo'] == 'F' or dados['sexo'] == 'M':
                break
            print(f'ERRO! Apenas [F/M]')

    #Validação
    while True:
        try:
            dados['idade'] = int(input('Idade: '))
            soma += dados['idade']
            break
        except ValueError:
            print(f'ERRO! Apenas números')

    #Faz uma cópia dos dados para "lista_pessoas"
    lista_pessoas.append(dados.copy())

    #Validação
    while True:
        try:
            encerramento = str(input('Quer continuar? [S/N]')).strip().upper()[0]
            if encerramento in 'SN':
                break
            print(f'ERRO! Por favor, digite apenas S ou N.')
        except IndexError:
            print(f'ERRO! Por favor, digite apenas S ou N.')

    #Encerramento
    if encerramento == 'N':
        break

print(f'{'='*30}')

#Faz a média das idades cadastradas.
media = soma / len(lista_pessoas)

print(f'A) Ao todo temos {len(lista_pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram', end=' ')
for p in lista_pessoas:
    if p["sexo"] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'Lista das pessoas que estão acima da média de idade:')

for p in lista_pessoas:
    if p['idade'] > media:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')

print('<<< ENCERRADO >>>')














