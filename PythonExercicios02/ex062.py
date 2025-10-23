#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar '0 termos'


print('Gerador de PA')
print('='*10)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro_termo #Qual é o termo
contador = 0
total_termos = 0

print('A PA é:', end=' ')
while contador < 10:
    print(f'{termo}', end=' ')
    print(f'>' if contador < 9 else '= FIM', end=' ')
    termo += razao
    contador += 1
    total_termos += 1
    if contador == 10:
        primeiro_termo = int(input('\nQuantos termos você quer mostrar a mais? (Digite 0 para sair): '))
        if primeiro_termo != 0:
            contador = 10 - primeiro_termo
        else:
            print(f'Progressão finalizada com {total_termos} termos mostrados.')




















