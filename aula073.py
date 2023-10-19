"""
Higher Order Functions
Funções de Primeira Classe
"""


# def saudacao(msg):
#     return msg

# saudacao_2 = saudacao


# v = saudacao_2('Bom dia')
# print(v)


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Bom dia', 'Julio')

print(v)
