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

s1 = set()
print(s1, type(s1))

s1 = set('Julio')
print(s1)

s1 = {'Julio', 1, 2, 3}
print(s1)
