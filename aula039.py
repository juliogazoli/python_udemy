"""
Iterando strings com while
"""
#       01234
nome = 'Julio' # Iteráveis
#      -54321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

# Exercício guiado
# Minha solução
# contador = 0
# nova_string = ""
# while contador < len(nome):
#     nova_string += '*'
#     nova_string += nome[contador]
#     contador += 1

# print(nova_string)


# Correção
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
