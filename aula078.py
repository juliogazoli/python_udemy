"""
Sets - Conjuntos em Python (tipo set)
Conjntos são ensinados na matemática
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitas apenas
tipos imutáveis como valor interno.

Criando um set
set(iterável) ou {1, 2, 3}


Sets são eficientes para remover valores duplicados
de iteráveis.
- eles não tem índeces;
- eles não garantem ordem;
- eles são iteráveis (for, in, not in)

Métodos úteis:
add, update, clear, discard
"""

# s1 = set()
# print(s1, type(s1))

# s1 = set('Julio')
# print(s1)

# s1 = {'Julio', 1, 2, 3}
# print(s1)


# s1 = {1, 2, 3, 3, 3, 3, 3, 1}
# print(s1)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# s1 = {1, 2, 3, [123]} # Erro: não aceita lista
# s1 = {1, 2, 3, {123}} # Erro: não aceita set
# s1 = {1, 2, 3, {'chave': 'valor'}} # Erro: não aceita set
# s1 = {1, 2, 3, (123,)} # Ok

s1 = {1, 2, 3}
for numero in s1:
    print(numero)
