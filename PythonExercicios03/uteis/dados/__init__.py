
def leiadinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        if entrada == '' or entrada.isalpha():
            print(f'\033[31mERRO! "{entrada}" é um preço inválido!\033[m')
        else:
            return float(entrada)




def leiaint(msg):
    #Loop de validação
    while True:
        try:
            inteiro = int(input(msg))
            return inteiro
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido\033[m')




def leiafloat(msg):
    while True:
        try:
            numero = float(input(msg))
            return numero
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número real válido\033[m')



























