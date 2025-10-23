#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior : APROVADO

primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))
media = (primeira_nota + segunda_nota) /2

print(f'Tirando {primeira_nota:.1f} e {segunda_nota:.1f}, a média do aluno é {media:.1f}')

if media <5:
    print('O aluno está REPROVADO.')

elif  5 <= media < 6.9: # SE media estiver entre 5 e 6.9
    print('O aluno está de RECUPERAÇÃO')

elif media >= 7:
    print('O aluno está APROVADO')









