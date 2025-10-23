Manipulando cadeias de texto

frase = 'curso em video python' #atribuição de uma string dentro de uma variável. #cada caractere dentro de '' é um índice


Fatiamento
frase[9] #símbolo '[]' é o identificador de uma estrutura de dados de python chamada LISTA

frase[9:13] #do 9º índice até o 12º # sempre um a menos no final

frase[9:13:2] #salta de 2 em 2 e ignora os que foram saltados

frase[:5] #antes do : é onde ele vai começar

frase[15:]# inicio no índice 15 até o final

frase[9::3]# 9º índice até o final, depois, pula de 3 em 3 e ignora os que foram saltados

Análise
len = lenght = comprimento
len(frase) #qual é o comprimento da frase

frase.count('o') #conte quantas vezes aparece a letra "o"
frase.count('o,0,13') #contagem já fatiado (do 0 até o 13(12)) último valor é sempre ignorado

frase.find(' ') #Procura a primeira ocorrência de um espaço em branco na string, se não encontrar espaço retorna -1. Se for '  ' com 2 espaços entre aspas ele conta a quantidade de espaços
frase.find('deo') #quantas vezes encontrou 'deo'
frase.find('android')#se não existe retorna -1

'curso'' in frase #true or false

Transformação
frase.replace('Python', 'Android')#procure por python e substitui por android
frase.upper()#o que for maiusculo mantém, o que não for é trocado
frase.lower()#contrário de upper
frase.capitalize()#todos os caracteres pra minusculos e o primeiro ficará em maiusculo
frase.title()#começo de frase em maiúsculo
frase.strip()#remove espaços inúteis no começo e no final da string
frase.rstrip()#remove somente os últimos espaços
frase.lstrip()#remove somente os primeiros espaço

Divisão
frase.split()#divisão considerando espaços vazios #remove índices vazios e cria listas novas onde ficavam os espaços #listas novas em cada frase

Junção
'-'.join(frase)#junta os elementos de frase e usa '-' assim gerando índices pra cada '-'

print('''
a
s
v
c
x
x
''')                   #''' começo e final ignorando linha