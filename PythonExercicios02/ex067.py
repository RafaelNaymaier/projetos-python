#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

contador = 0

#Loop principal
while True:
    print('-'*35)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    #Se valor for negativo, sai do loop.
    if valor < 0:
        break

    #Mostra ao usuário a tabuada até 10.
    while True:
        contador += 1
        print(f'{valor} x {contador} = {valor*contador}')
        if contador == 10:
            contador = 0
            break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')




















