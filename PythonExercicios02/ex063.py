#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma sequência de Fibonacci.
#Ex: 0, 1, 1, 2, 3, 5, 8



num1 = 0
num2 = 1
num3 = num1 + num2

termos = int(input('Quantos termos você quer mostrar?'))
contador = -2 +termos

#print('~'*30)
print(f'{num1} > {num2} >',end=' ')

while contador !=0:
    num1 = num2 # Vira 1 no primeiro loop
    num2 = num3 # Vira 1 no primeiro loop
    print(num2, end=' ')
    print('> FIM' if contador == 1 else '>', end=' ')
    num3 = num1 + num2
    contador -= 1
#print('~'*30)

'''num1 = 0 #Inicia variável com 0
num2 = 1 #Inicia variável com 1

termos = int(input('Digite quantos termos você quer mostrar?')) #Pergunta ao usuário

if termos >= 1: #Se a quantidade de termos for igual ou maior que 1
    print(f'{num1}', end=' ') #Escreva

    if termos >= 2: #Se a quantidade de termos for igual ou maior que 1
        print(f'> {num2}', end=' ') #Escreva

        contador = 2 #Inicia a variável contador com 2
        while contador < termos: #Enquanto 'contador' for menor que 'termos'...
            num3 = num1 + num2       #Num3 passa a ser a soma de num1 e num2
            print(f'> {num3}', end=' ') #Escreva

            num1 = num2 #Variável num1 recebe num2, que é o necessário para a próxima sequência
            num2 = num3

            contador += 1 #Conta +1 ao 'contador', para que quando fique maior que 'termos', pare o while, que está fazendo a sequência de fibonacci'''



































