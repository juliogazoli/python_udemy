"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""


# def soma(x, y):
#     print(x + y)


# soma(1, 2)
# soma(3, 5)
# soma(100, 200)


# def soma(x, y, z=0):
#     print(f'{x=} {y=} {z=}', x + y + z)


# soma(1, 2)
# soma(3, 5)
# soma(100, 200)


# def soma(x, y, z=0):
#     if z:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)
        

# soma(1, 2)
# soma(3, 5)
# soma(100, 200)
# soma(7, 9, 0)


def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
        

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=7, z=0, x=7)
