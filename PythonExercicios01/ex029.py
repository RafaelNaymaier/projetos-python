#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7.00 por cada km acima do limite

from colorama import Style, Fore, Back

velocidade = float(input('Qual é a velocidade atual do carro?')) #Pergunta ao usuário a velocidade do carro




if velocidade > 80: #Se o valor digitado pelo usuário for maior que 80
    print(Fore.RED + 'MULTADO! Você excedeu o limite permitido que é de 80Km/h' + Style.RESET_ALL)
    print(Fore.RED + 'Você deve pagar uma multa de ' + Fore.YELLOW + 'R$ {:.2f}'.format((velocidade-80)*7)+ Style.RESET_ALL)

else: #Se não
    print (Fore.LIGHTYELLOW_EX + 'Tenha um bom dia! Dirija com segurança!' + Style.RESET_ALL)