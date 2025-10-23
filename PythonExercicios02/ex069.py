#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

print('-'*35,'\nCADASTRE UMA PESSOA\n', '-'*35, sep='')

quantidade_pessoas = 0
quantidade_homens = 0
quantidade_mulheres = 0

#Loop principal.
while True:

    #Valida idade.
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('Digite um valor valido')

    #Valida sexo
    while True:
        try:
            sexo = str(input('Sexo: [M/F] ')).upper()[0]
            if sexo == 'M' or sexo == 'F':
                break
            else:
                print('Digite um sexo válido.')
        except (ValueError,TypeError, IndexError):
            print('Digite um sexo válido.')
    print('-'*35)

    #Valida encerramento do programa.
    while True:
        try:
            encerramento = str(input('Quer continuar? [S/N] ')).upper()[0]
            if encerramento == 'S' or encerramento == 'N':
                break
            else:
                print('Resposta inválida.')
        except (ValueError,TypeError, IndexError):
            print('[S/N]')
    print('-'*35)

    #Atualiza as contagens.
    if idade >= 18:
        quantidade_pessoas += 1
    if sexo == 'M':
        quantidade_homens += 1
    elif sexo == 'F' and idade < 20:
        quantidade_mulheres += 1
    if encerramento == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {quantidade_pessoas}')
print(f'Ao todo temos {quantidade_homens} homens cadastrados')
print(f'E temos {quantidade_mulheres} mulheres com menos de 20 anos')





















