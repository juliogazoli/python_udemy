"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item no final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas
Create Read Update  Delete
Criar  Ler  Alterar Apagar = lista[i] (CRUD)
"""


########## PARTE 01 ##########
#         01234
#        -54321
# string = 'ABCDE' # 5 caracteres (len)
# # print(bool([])) # falsy
# # print(lista, type(lista))

# #        0    1      2       3    4
# #       -5   -4     -3      -2   -1
# lista = [123, True, 'Julio', 1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))


########## PARTE 02 ##########
#        0   1   2   3   4   5
# lista = [10, 20, 30, 40]
# # lista[2] = 300
# # del lista[2]
# # print(lista)
# # print(lista[2])
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista, 'Removido:', ultimo_valor)


########## PARTE 03 ##########
#        0   1   2   3
# lista = [10, 20, 30, 40]
# lista.append('Julio')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(100, 5)
# print(lista[4])


########## PARTE 04 ##########
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_a)


########## PARTE 05 ##########
"""
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Julio'
# outra_variavel = nome
# nome = 'João'
# print(nome)
# print(outra_variavel)

# lista_a = ['João', 'Maria']
# lista_b = lista_a

# lista_a[0] = 'Qualquer coisa'
# print(lista_b)

lista_a = ['João', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
