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

Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
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

# s1 = {1, 2, 3}
# for numero in s1:
#     print(numero)


# s1 = set()
# s1.add('Julio')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Olá mundo')
# print(s1)


s1 = {1, 2, 3}
s2 = {2, 3, 4}
# s3 = s1 | s2 # union
# s3 = s1 & s2 # intersection
# s3 = s1 - s2 # diferença
# s3 = s2 - s1 # diferença
s3 = s2 ^ s1 # diferença simétrica
print(s3) 
