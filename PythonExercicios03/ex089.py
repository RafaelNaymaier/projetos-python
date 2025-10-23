#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunos = []
dados = []

#Loop principal.
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    media = (dados[1] + dados[2])/2
    dados.append(media)
    lista_alunos.append(dados[:])
    dados.clear()

    #Encerramento do programa.
    encerramento = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if encerramento == 'N':
        print(f'{'-'*30}')
        break

print(f'{'No.':<5} {'NOME':^10} {'MÉDIA':^7} \n{'-'*30}')

#Mostra nome e a média do aluno.
for n, aluno in enumerate(lista_alunos):
    print(f'{n:<5} {aluno[0]:^10} {aluno[3]:^7}')
print(f'{'-'*30}')

#Mostra as notas individuais de cada aluno.
while True:
    escolhe_notas = int(input(f'Mostrar notas de qual aluno? [999 para parar]'))
    if escolhe_notas == 999:
        break
    if escolhe_notas <= len(lista_alunos)-1:
        print(f'Notas de {lista_alunos[escolhe_notas][0]} são [{lista_alunos[escolhe_notas][1]}, {lista_alunos[escolhe_notas][2]}]')
    else:
        print(f'O aluno não existe!')






















