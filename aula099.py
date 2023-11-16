"""
https://stackoverflow.com/questions/2386714/why-is-import-bad
"""
# from sys import path

# import aula099_package.modulo
# from aula099_package import modulo
# from aula099_package.modulo import soma_do_modulo
# from aula099_package.modulo import *

# # print(*path, sep='\n')
# print(aula099_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(soma_do_modulo(1, 2))
# print(variavel)
# # print(nova_variavel)


# from aula099_package.modulo import soma_do_modulo, fala_oi
# print(__name__)
# fala_oi()


# import aula099_package
from aula099_package import soma_do_modulo, falar_oi

# print(aula099_package.dobra(2))
# print(aula099_package.soma_do_modulo(2, 3))
print(soma_do_modulo(2, 3))
falar_oi()
