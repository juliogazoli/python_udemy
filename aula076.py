"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}
print(pessoa, type(pessoa))
"""

# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

# # print(pessoa, type(pessoa))
# # print(pessoa['nome'])

# # for chave in pessoa:
# #     print(chave)

# for chave in pessoa:
#     print(chave, pessoa[chave])


"""
Manipulando chaves e valores em dicionários
"""

# pessoa = {}

# # pessoa['nome'] = 'Luiz Otávio'
# # print(pessoa['nome'])

# chave = 'nome'
# pessoa[chave] = 'Luiz Otávio'
# print(pessoa[chave])

# pessoa[chave] = 'Maria'

# pessoa['sobrenome'] = 'Miranda'

# print(pessoa)

# # del pessoa['sobrenome']

# print(pessoa)

# # print(pessoa.get('sobrenome', 'Não existe'))

# # if pessoa.get('sobrenome'):
# #     print('Existe')


# if pessoa.get('sobrenome') is None:
#     print('Não existe')
# else:
#     print(pessoa['sobrenome'])


"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave espedificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda 1',
#     'sobrenome': 'Miranda 2',
#     'sobrenome': 'Miranda 3',
# }

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
}

# print(pessoa.__len__())
# print(len(pessoa))

# print(pessoa.keys())
# print(tuple(pessoa.keys()))
# print(list(pessoa.keys()))

# print(pessoa.values())

# print(pessoa.items())

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa.setdefault('idade', None)
print(pessoa['idade'])