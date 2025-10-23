#Dicionários

#dados = dict
'''dados = {'nome':'Pedro', 'idade':25}

dados['sexo'] = 'M'

print(dados)'''

'''Diferença entre valor chave e item'''

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
}

print(filme.values()) #Retorna todos os valores

print(filme.keys()) #Retorna o nome das 'categorias' dos valores

print(filme.items()) #Retorna tudo

for k, v in filme.items():
    print(f'O {k} é {v}')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

#Adicionar
pessoas['peso'] = 98.5

#Modificar
pessoas['nome'] = 'Luciana

del pessoas['sexo']
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos.')

for k, v in pessoas.items():
    print(f'{k} = {v}')


#Lista com dicionario
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ',}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])










