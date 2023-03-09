"""
Exercício
Exiba os índices da lista
0 maria
1 Helena
2 Luiz
"""
# Minha solução:
# lista = ['Maria', 'Helena', 'Luiz']

# contador = 0
# while contador < len(lista):
#     print(f'Índice {contador} - {lista[contador]}')
#     contador += 1

# Solução:
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
