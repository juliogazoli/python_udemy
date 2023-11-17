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

# Minha Solução
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']


def zipper(lista_1, lista_2):
    nova_lista = []
    for indice, lista in enumerate(lista_1):
        nova_lista.append((lista, lista_2[indice]))
    return nova_lista


z = zipper(cidades, estados)
print(z)
