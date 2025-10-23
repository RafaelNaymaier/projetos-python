#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
#Palíndromo é uma frase que pode ser lida de tras para frente EX: após a sopa, a sacada da casa, o lobo ama o bolo
#a sacada da casa

#Minha versão
'''frase = str(input('Digite uma frase: ')).upper().strip().replace(' ', '')

invertida = frase[::-1]

print(f'O inverso de {frase} é {invertida}')

if frase == invertida:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''

#Versão do vídeo
frase = str(input('Digite uma frase: ')).upper().strip().split()
junto = ''.join(frase) #Função .replace (' ', '') faz a mesma coisa

inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')













