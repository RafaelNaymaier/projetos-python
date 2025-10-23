#Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'f'
#Caso esteja errado, peça a digitação novamente até ter um valor correto


fim = 1
while fim != 0:
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
    if sexo == 'F' or sexo == 'M':
        print (f'Sexo {sexo} registrado com sucesso.')
        fim = 0
    else:
        print('Dados inválidos. Por favor, informe seu sexo.')

'''fim = 1
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while fim != 0:
    if sexo == 'F' or sexo == 'M':
        print (f'Sexo {sexo} registrado com sucesso.')
        fim = 0
    else:
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo.')).strip().upper()'''














