"""
Problema dos parâmetros mutáveis em funções Python
"""


def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente_1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', cliente_1)
adiciona_clientes('Fernando', cliente_1)
cliente_1.append('Edu')
print(cliente_1)

clientes_2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', clientes_2)
print(clientes_2)

clientes_3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', clientes_3)
print(clientes_3)
