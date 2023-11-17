"""
Exercícios
"""

import copy

from dados import produtos

print('PRODUTOS')
print(*produtos, sep='\n')

"""
Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)
"""
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

print()
print('NOVOS PRODUTOS')
print(*novos_produtos, sep='\n')


"""
Ordene os produtos por nome decrescente (do maior para o menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
"""
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print()
print('PRODUTOS ORDENADOS POR NOME')
print(*produtos_ordenados_por_nome, sep='\n')


"""
Ordene os produtos por preço crescente (do menor para o maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

print()
print('PRODUTOS ORDENADOS POR PRECO')
print(*produtos_ordenados_por_preco, sep='\n')
