"""
Generator expression, Iterables e Iterators em Python
"""
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)

lista = [n for n in range(1000000)]
print(sys.getsizeof(lista))

generator = (n for n in range(1000000))
# print(generator)
print(sys.getsizeof(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# for n in generator:
#     print(n)
