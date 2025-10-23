

Entrada de dados
nome = input("Digite seu nome: ")
print("Olá,", nome)

'''Listas''' #Armazenam vários valores:
frutas = ["maçã", "banana", "uva"]

print(frutas[0])  # maçã
print(frutas[1])  # banana

frutas.append("laranja")  # adiciona na lista
print(frutas)

'''Funções''' #Servem para organizar código e reutilizar:
def saudacao(nome):
    print("Olá,", nome)

saudacao("João")
saudacao("Maria")

'''Variáveis e tipos de dados'''

'''As variáveis são um dos conceitos mais importantes e fundamentais na programação.
Pense nelas como contêineres ou caixas com etiquetas que você usa para guardar informações no seu programa.
O nome "variável" vem do fato de que o valor que ela contém pode mudar (ou variar) ao longo do tempo.
Toda variável tem três partes principais:'''

'''1. Nome

É a "etiqueta" na sua caixa. O nome da variável é o que você usa para se referir ao dado que ela guarda.
Regras para nomes de variáveis no Python:
Devem começar com uma letra (a-z, A-Z) ou um sublinhado (_).
Não podem começar com um número.
Só podem conter caracteres alfanuméricos (a-z, A-Z, 0-9) e sublinhados.
São sensíveis a maiúsculas e minúsculas (idade é diferente de Idade).
Nomes de variáveis em Python geralmente são escritos em letras minúsculas, com palavras separadas por sublinhados (meu_nome).'''

'''2. Valor
É o que está "dentro da caixa". Você atribui um valor a uma variável usando o sinal de igual (=).'''
# A variável 'idade' recebe o valor 30
idade = 30

'''3. Tipo
É o "tipo de dado" do valor que a variável guarda, como texto, número inteiro, número decimal, etc. O Python descobre o tipo automaticamente.'''
# Essa variável guarda um número inteiro (int)
numero_inteiro = 10

# Essa guarda um texto (str)
meu_nome = "João"

# Essa guarda um número decimal (float)
altura = 1.75

'''Exemplo Prático'''
# Criando uma variável chamada 'nome' com o valor "Ana"
nome = "Ana"

# A variável 'nome' tem o valor "Ana"
print(nome)

# O tipo da variável 'nome' é string (str)
print(type(nome))

# Agora, a variável 'nome' recebe um novo valor, que é um número.
# O Python muda o tipo automaticamente.
nome = 25

# A variável 'nome' agora tem o valor 25
print(nome)

# O tipo da variável 'nome' agora é inteiro (int)
print(type(nome))

'''Indexação aninhada'''

'''A Analogia da Caixa
Pense na indexação aninhada como uma caixa dentro de outra caixa.
O primeiro índice ([ ]) abre a primeira caixa e te leva para a caixa que está dentro dela.
O segundo índice ([ ]) abre essa segunda caixa para você pegar o item que está lá dentro.
A chave para usar a indexação aninhada é que o item que você pega com o primeiro índice tem que ser, ele próprio, uma sequência (como uma string, uma lista ou outra tupla).'''

'''1. Acessando um item em uma Lista de Listas'''
# Isto é uma lista que contém outras 3 listas
cardapio = [
    ['Arroz', 'Feijão'],    # índice 0
    ['Macarrão', 'Salada'],  # índice 1
    ['Bife', 'Frango']       # índice 2
]

# Pegar 'Macarrão' (está no índice 0 da lista no índice 1)
item = cardapio[1][0]
print(item)  # Saída: Macarrão

'''2. Acessando um item em uma Tupla de Tuplas'''
# Esta é uma tupla que contém outras 3 tuplas
ponto_cartografico = (
    (10, 20),  # índice 0
    (30, 40),  # índice 1
    (50, 60)   # índice 2
)

# Pegar o valor '40' (está no índice 1 da tupla no índice 1)
valor_y = ponto_cartografico[1][1]
print(valor_y)  # Saída: 40

'''3. Acessando um caractere dentro de uma palavra'''
palavras = ('Python', 'Java')

# Para pegar a letra 'J', que está na posição 0 da palavra no índice 1
primeira_letra_de_java = palavras[1][0]
print(primeira_letra_de_java)  # Saída: J


'''Operadores lógicos'''

#Esses operadores são usados para combinar expressões lógicas e criar condições mais complexas.
#O resultado é também um valor booleano (True ou False).

and: # A condição só será True se ambas as partes forem True
if idade > 18 and tem_carro == True:
  print("Pode dirigir!")

or: # A condição será True se uma das partes for True
if temperatura > 30 or esta_chovendo == False:
  print("Vamos para a piscina!")

not: # A condição 'not False' se torna True
if not esta_chovendo:
  print("Vamos sair!")

float - números reais ou números de ponto flutuante ex= 4.5, -0.05 7.0
bool - valores lógicos ou boleanos ex= True ou False
str - valor caractere ou string ex= 'Olá', '7.5' ''

'''Operadores Aritméticos'''
#Usados para fazer cálculos matemáticos.

+ (adição): 10 + 5 resulta em 15
- (subtração): 10 - 5 resulta em 5
* (multiplicação): 10 * 5 resulta em 50
/ (divisão): 10 / 5 resulta em 2.0 (sempre retorna um float)
% (módulo): 10 % 3 resulta em 1 (retorna o resto da divisão)
** (exponenciação): 2 ** 3 (2 elevado a 3) resulta em 8
// (divisão inteira): 10 // 3 resulta em 3 (ignora as casas decimais)


'''Operadores de Atribuição'''
#Usados para atribuir um valor a uma variável.

= (atribuição): idade = 25
+= (adição e atribuição): x += 5 é o mesmo que x = x + 5
-= (subtração e atribuição): x -= 5 é o mesmo que x = x - 5

'''Operadores de Comparação'''
#Usados para comparar dois valores. O resultado é sempre um valor booleano (True ou False).

== (igual a): 10 == 10 resulta em True
!= (diferente de): 10 != 5 resulta em True
> (maior que): 10 > 5 resulta em True
< (menor que): 10 < 5 resulta em False
>= (maior ou igual a): 10 >= 10 resulta em True
<= (menor ou igual a): 5 <= 10 resulta em True



'''Tratamento de erros'''

'''O Básico: try e except
O código que você quer tentar executar vai no bloco try.
O código para lidar com o erro (o "Plano B") vai no bloco except.
Se o código no try rodar sem nenhum problema, o except é totalmente ignorado. Mas se um erro ocorrer no try, o Python para de executar aquele bloco e vai direto para o except.
Exemplo:
Imagine que você pede um número ao usuário, mas ele digita um texto. Sem o try...except, o programa iria quebrar.'''

# Versão sem tratamento de erro (pode dar erro!)
# idade = int(input('Digite sua idade: '))

# Versão com tratamento de erro
try:
  idade = int(input('Digite sua idade: '))
  print(f'Sua idade é {idade}')
except:
  print('Isso não é um número válido!')

'''Tipos de Erro
Você pode ser mais específico e tratar apenas tipos de erros que você espera. 
Por exemplo, o erro de converter texto para número é um ValueError.'''

try:
  idade = int(input('Digite sua idade: '))
  print(f'Sua idade é {idade}')
except ValueError:
  print('O valor digitado não pode ser convertido para número!')

else e finally
'''Você pode adicionar dois blocos opcionais ao seu try...except para ter ainda mais controle:'''
else: '''O código aqui é executado apenas se o bloco try for bem-sucedido e nenhum erro ocorrer.'''
finally: '''O código aqui sempre será executado, não importa se houve um erro ou não. É útil para tarefas de limpeza, como fechar um pastas.'''

try:
  idade = int(input('Digite sua idade: '))
except ValueError:
  print('O valor digitado não é um número.')
else:
  print('A entrada foi válida. Que bom!')
finally:
  print('Obrigado por usar o programa!')

'''Estrutura de repetição (loops)'''

#for → quando sabemos quantas vezes repetir:
    times = ['Flamengo', 'Palmeiras', 'São Paulo']

    for time in times:
      print(time)

    # Saída:
    # Flamengo
    # Palmeiras
    # São Paulo

#while →  repete enquanto a condição for verdadeira:
    numero = 0

    while numero < 5:
      print(numero)
      numero += 1 # O mesmo que 'numero = numero + 1'

    # Saída:
    # 0
    # 1
    # 2
    # 3
    # 4

'''Comandos de Controle de Loop'''

#break: Sai do loop imediatamente, mesmo que a condição ainda seja verdadeira.
    for i in range(10):
      if i == 3:
        break # O loop vai parar quando i for 3
      print(i)

    # Saída:
    # 0
    # 1
    # 2

#continue: Pula a iteração atual e passa para a próxima.
    for i in range(5):
      if i == 2:
        continue # Pula a impressão quando i for 2
      print(i)

    # Saída:
    # 0
    # 1
    # 3
    # 4



'''Organização'''

    (end='')  #não quebra linha, pode ser colocado qualquer coisa entre ''
     (\n)         #nova linha
    ({:.3f})     # caso precise limitar casas decimais
    sep='' #você está dizendo para o Python não usar nada (uma string vazia) para separar os itens.

'''lógica'''

    O operador and tem uma lógica diferente. Ele só retorna '''Verdadeiro''' se as duas partes forem verdadeiras.

'''Funções imbutidas (built-in functions)'''
#Funções evitam a repetição do código


#Funções matemáticas e lógicas.
    min() - Retorna o menor valor
    numeros_sorteados = (5, 2, 8, 1)
    menor_valor = min(numeros_sorteados)

    sum() - Soma todos os valores
    numeros_sorteados = (5, 2, 8, 1)
    soma_total = sum(numeros_sorteados)
    print(f"A soma de todos os valores é: {soma_total}")

    abs(): Retorna o valor absoluto de um número.
    print(abs(-10)) # Saída: 10

#Funções para Trabalhar com Coleções
    len() - Conta o número de itens
    numeros_sorteados = (5, 2, 8, 1)
    quantidade_de_numeros = len(numeros_sorteados)

    sorted(): Retorna uma nova lista com os itens de uma coleção em ordem.
    numeros = [3, 1, 2]
    print(sorted(numeros))  # Saída: [1, 2, 3]

    range(): Cria uma sequência de números, muito útil em loops for.
    for i in range(3):
        print(i) # Imprime 0, 1, 2

#Funções de entrada ou saída.
    print(): Imprime uma mensagem ou o valor de uma variável no console.
    print("Olá, mundo!")

    input(): Pede para o usuário digitar algo e retorna o texto digitado.
    nome = input("Digite seu nome: ")

#Funções de Tipo.
    int(): Converte um valor para um número inteiro.
    numero = int("10")

    float(): Converte um valor para um número decimal (com ponto flutuante).
    numero_decimal = float("5.5")

    str(): Converte um valor para texto (string).
    texto = str(123)

    type(): Retorna o tipo de um objeto ou variável.
    print(type("abc"))

'''Métodos de Formatação de Texto'''

    upper(): Transforma todas as letras da string em maiúsculas.
    texto = "olá, mundo!"
    print(texto.upper())  # Saída: OLÁ, MUNDO!

    lower(): Transforma todas as letras em minúsculas.
    texto = "OLÁ, MUNDO!"
    print(texto.lower())  # Saída: olá, mundo!

    capitalize(): Transforma a primeira letra da string em maiúscula e o resto em minúscula.
    texto = "olá, mundo!"
    print(texto.capitalize())  # Saída: Olá, mundo!

    title(): Transforma a primeira letra de cada palavra em maiúscula.
    texto = "eu sou a lua"
    print(texto.title())  # Saída: Eu Sou A Lua

'''Métodos de Verificação e Busca'''

    startswith(): Verifica se a string começa com um determinado texto.
    frase = "Python é legal."
    print(frase.startswith("Python"))  # Saída: True

    endswith(): Verifica se a string termina com um determinado texto.
    frase = "Python é legal."
    print(frase.endswith("legal."))  # Saída: True

    find(): Encontra a primeira ocorrência de um texto dentro da string e retorna o seu índice (posição). Se não encontrar, retorna -1.
    frase = "Olá, mundo!"
    print(frase.find("mundo"))  # Saída: 5

'''Métodos de Manipulação de Texto'''

    strip(): Remove espaços em branco do início e do fim da string.
    texto = "  espaço  "
    print(texto.strip())  # Saída: espaço

    replace(): Substitui todas as ocorrências de um texto por outro.
    frase = "Olá, mundo!"
    print(frase.replace("mundo", "Python"))  # Saída: Olá, Python!

    split(): Divide a string em uma lista de substrings.
    frase = "maçã,banana,laranja"
    print(frase.split(','))  # Saída: ['maçã', 'banana', 'laranja']

    join(): Junta os itens de uma coleção em uma única string.
    palavras = ['Olá', 'mundo']
    print(' '.join(palavras))  # Saída: Olá mundo


'''validação'''

    try:
        # código que pode falhar
    except ValueError:
        # o que fazer se o erro ValueError acontecer

    ValueError: #Acontece quando a função int() ou float() recebe um texto que não pode ser convertido num número (ex: o usuário digita "olá").

    TypeError: #Acontece quando uma operação é feita com um tipo de dado errado (ex: tentar somar um número com um texto).

    ZeroDivisionError: #Acontece quando tentamos dividir um número por zero.

'''Estrutura de decisões (if else)'''

    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

     '''Estrutura condicional aninhada'''
        nome = str(input('Qual é seu nome? '))
        if nome == 'Gustavo':
            print('Que nome bonito!')
        elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
            print('Seu nome é bem popular no Brasil.')
        elif nome in 'Ana Cláudia Jéssica Juliana':
            print('Belo nome feminino!')
        else:
            print('Seu nome é bem normal.')
        print('Tenha um bom dia, {}!'.format(nome))


'''Ordem de precedência'''
1 - ()
2 - **
3 - '*'   '/'   '//'   '%'
4 - '+'   '-'

'''Calcular porcentagem'''

#no caso de desconto
    preço - (preço * 5 / 100) #onde 5 é a 5%
    preço x 0.95 # onde 0.95 é 5%

#no caso de aumento
    preço + (preço *5 /100) # onde 5 é 5%
    preço x1.05 # onde 1.05 é 5%

'''Cálculos para divisão real e resto de divisão'''

    divisão real = 100//100  = 1 pois 100 cabe 1 vez dentro de 100  OU 100/100 = 1
    resto de divisão 23%10 =  3   é o resultado pois é o resto da divisão, 23/10 = 2.3  porém 2 é ignorado pois é real

    5+3*2=11      # 3x2 primeiro  (3x2=5)+5=11
    3*5+4**2=31 # 4**2 primeiro, 3*5 segundo + resultado (16+15=31)
    3*(5+4)**2     # 5+4 primeiro,  2** segundo 3* terceiro (5+4=9**=81*3=243)

'''Operadores aritiméticos''' #Operadores precisam de dois operandos

    a = 10
    b = 3
    print(a + b)   # soma → 13
    print(a - b)   # subtração → 7
    print(a * b)   # multiplicação → 30
    print(a / b)   # divisão → 3.333...
    print(a // b)  # divisão inteira → 3
    print(a % b)   # resto da divisão → 1
    print(a ** b)  # potência → 1000

'''Operadores exponenciação'''

    '**' Potência                                 5**2==25
    '//' Divisão inteira                         5//2==2
    '%' Módulo ou resto da divisão    5%2==1

'''Hipotenusa'''

    Hipotenusa é a raiz quadrada da soma dos quadrados dos catetos
    cateto1 = float(input("Digite o valor do primeiro cateto: "))
    cateto2 = float(input("Digite o valor do segundo cateto: "))
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

    import math
    cateto1 = float(input("Digite o valor do primeiro cateto: "))
    cateto2 = float(input("Digite o valor do segundo cateto: "))
    hipotenusa = math.hypot(cateto1, cateto2)

    print("A hipotenusa é:", hipotenusa

'''Índices'''

Em Python, índices negativos contam de trás para frente:
    [-1]: último elemento
    [-2]: penúltimo elemento
    etc.
    and → Ambas verdadeiras
    or → Pelo menos uma verdadeira

    Divisivel #Se valor é divisivel por 4
    valor % 4 ==0

    f-strings (ou formatted string literals) são a forma mais prática e moderna de formatar texto no Python.
    nome = "Maria"
    idade = 25

    print(f"Meu nome é {nome} e tenho {idade} anos.")

cor = ('\033[0m',        # 0 - Sem cores (reset)
       '\033[0;30;41m', # 1 - Fundo Vermelho
       '\033[0;30;42m', # 2 - Fundo Verde
       '\033[0;30;43m', # 3 - Fundo Amarelo
       '\033[0;30;44m', # 4 - Fundo Azul
       '\033[0;30;45m', # 5 - Fundo Magenta
       '\033[0;30;46m', # 6 - Fundo Ciano
       '\033[0;30;47m'  # 7 - Fundo Branco
)






       )
