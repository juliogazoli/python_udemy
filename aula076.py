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

pessoa = {}

# pessoa['nome'] = 'Luiz Otávio'
# print(pessoa['nome'])

chave = 'nome'
pessoa[chave] = 'Luiz Otávio'
print(pessoa[chave])

pessoa[chave] = 'Maria'

pessoa['sobrenome'] = 'Miranda'

print(pessoa)

# del pessoa['sobrenome']

print(pessoa)

# print(pessoa.get('sobrenome', 'Não existe'))

# if pessoa.get('sobrenome'):
#     print('Existe')


if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
