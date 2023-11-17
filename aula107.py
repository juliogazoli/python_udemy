"""
Exercício - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado:
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""

# # Minha Solução
# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']


# def zipper(lista_1, lista_2):
#     nova_lista = []
#     for indice, lista in enumerate(lista_1):
#         nova_lista.append((lista, lista_2[indice]))
#     return nova_lista


# z = zipper(cidades, estados)
# print(z)


# Solução
# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [
#         (l1[i], l2[i]) for i in range(intervalo)
#     ]


# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(l1, l2))


# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']

# print(list(zip(l1, l2)))


from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))
