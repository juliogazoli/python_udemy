"""
Desempacotamento em chamadas de métodos e funções
"""

string = 'ABCD'
# lista = ['Maria', 'Helena', 'Eduarda']
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda',],
]

# a, b, c = lista
# a, b, c, *_ = lista # '*_' recebe o restante do desempacotamento
# a, b, *_, u = lista
# print(a, u)

# for nome in lista:
#     print(nome, end=' ')

# print(*lista)
# print(*string)
# print(*tupla)
# print(*salas)
print(*salas, sep='\n')
