# Operadores in e not in
# String são iteráveis
# 0 1 2 3 4
# J u l i o
# 5 4 3 2 1

# nome = 'Julio'

# print(nome[2])
# print(nome[-3])

# print('u' in nome)
# print('lio' in nome)
# print(10 * '-')
# print('lio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
