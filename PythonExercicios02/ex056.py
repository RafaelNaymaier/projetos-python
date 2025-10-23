#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos.

print('-'*5, f'1ª pessoa', '-'*5)
nome = str(input('Nome: ')).strip()
idade = int(input('Idade: '))
sexo = str(input('Sexo [M/F]: ')).strip().upper()

nome_velho = nome # 'nome_velho' recebe nome
maior_idade = idade # 'maior 'recebe o valor de idade para verificar quem tem a maior idade
soma_idade = idade # 'soma_idade' recebe valor de idade para verificar média no futuro
num_mulheres = 0 # 'num_mulheres' abre variável para verificar o número de mulheres abaixo de 20 anos no futuro
soma_mulheres = 0

if sexo == 'F' and idade <20:
    num_mulheres += 1
    soma_mulheres += idade

for c in range (2, 5):
    print('-'*5, f'{c}ª pessoa', '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade         #Soma todas as idades
    if idade > maior_idade :      #Verifica se idade > maior_idade
        maior_idade = idade       #Maior idade recebe idade
        nome_velho = nome
    if sexo == 'F' and idade <20:
        num_mulheres += 1
        soma_mulheres += idade

media = soma_idade / 4
media_mulheres = soma_mulheres / num_mulheres

print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maior_idade} anos e se chama {nome_velho}')

if num_mulheres > 0 :
    print(f'Ao todo são {num_mulheres} mulheres com menos de 20 anos e a média de idade é {media_mulheres}')
else:print('Não há mulheres com menos de 20 anos')

















