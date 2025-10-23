#Faça um programa que calcule a soma entre todos os números ímpares que são múltiploes de três e que se encontram no intervalo de 1 até 500.

#Inicialização de variável
quantidade = 0
soma = 0

for c in range(1,501,2): #Percorre todos os números de 1 a 501 pulando de 2 em 2, ou seja, apenas os ímpares.
    if c % 3==0:            # Verifica se o número é múltiplo de 3.
        soma += c          #Soma os números que satisfazem os dois critérios.
        quantidade += 1 #Conta quantos números foram somados.

print(f'A soma de todos os {quantidade} valores foi {soma} ') #Exibe a quantidade de números e a soma.
















