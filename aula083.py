"""
Empacotamento e desempacotamento de dicionários
"""

# a, b = 1, 2
# a, b = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }

# a, b = pessoa
# print(a, b)

# a, b = pessoa.values()
# print(a, b)

# a, b = pessoa.items()
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(valor)


# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }

# dados_pessoa = {
#     'idade': 16,
#     'altura': 1.6,
# }

# pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)


"""
args e kwargs
args (já vimos)
kwargs - keyword arguments (argumentos nomeados)
"""


# def mostra_argumentos_nomeados(*args, **kwargs):
#     print(kwargs)


# mostra_argumentos_nomeados(nome='Joana', qlq=123)


# def mostra_argumentos_nomeados(*args, **kwargs):
#     print('NÃO NOMEADOS:', args)

#     for chave, valor in kwargs.items():
#         print(chave, valor)


# mostra_argumentos_nomeados(1, 2, nome='Joana', qlq=123)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}


def mostra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostra_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostra_argumentos_nomeados(**configuracoes)
