#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntando ao utilizador se ele quer ou não continuar a digitar valores

vezes = soma = 0  # Inicia as variáveis 'vezes' e 'soma' com 0.

while True:  # Loop principal do programa.
    while True:
        try:
            numero = int(input('Digite um número: '))  # Tenta converter a entrada para um número inteiro.
            break  # Sai do loop de validação se a entrada for válida.
        except (ValueError, TypeError):
            print('Apenas números inteiros.')  # Em caso de erro, avisa o usuário e repete a pergunta.

    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()

    # Se a resposta for inválida, o número é desconsiderado.
    if pergunta != 'S' and pergunta != 'N':
        print('Resposta inválida. Número desconsiderado.')

    else:
        soma += numero
        vezes += 1

        # Define o primeiro número como o maior e o menor.
        if vezes == 1:
            menor = maior = numero

        # Atualiza o maior e o menor número a cada entrada.
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

        # Se a resposta for 'N', termina o programa.
        if pergunta == 'N':
            break

media = soma / vezes
print(f'Você digitou {vezes} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')















