"""
Introdução às Generator functions em Python
generator = (n for n in range(1000000))
"""


# def generator(n=0):
#     return 1


# gen = generator(n=0)
# print(gen)


# def generator(n=0):
#     yield 1 # Pausar
#     return 'ACABOU'


# gen = generator(n=0)
# # print(gen)
# # print(gen.__iter__())
# print(next(gen))
# print(next(gen)) # StopIteration: ACABOU


# def generator(n=0):
#     yield 1 # Pausar
#     print('Continuando...')
#     yield 2 # Pausar
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar')
#     return 'ACABOU'


# # gen = generator(n=0)
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# gen = generator(n=0)
# for n in gen:
#     print(n)


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


# gen = generator()
gen = generator(maximum=1000000)
for n in gen:
    print(n)
