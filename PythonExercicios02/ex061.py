#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura WHILE

print('Gerador de PA')
print('='*10)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro_termo #Qual é o termo
contador = 0

print('A PA é:', end=' ')
while contador < 10:
    print(f'{termo}', end=' ')
    print(f'>' if contador < 9 else '= FIM', end=' ')
    termo += razao
    contador += 1


















