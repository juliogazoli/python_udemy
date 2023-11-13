"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definição
# def soma(x, y):
#     # print(x + y)
#     print(f'{x=} y={y}', '|', 'x + y = ', x + y)


# # print(soma)
# # print(soma(1, 2))
# soma(1, 2)
# soma(2, 1)
# soma(y=2, x=1)


def soma(x, y, z):
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(y=2, z=3, x=1)
soma(1, 2, z=5)
soma(1, y=2, z=5)
