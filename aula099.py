from sys import path

import aula099_package.modulo
from aula099_package import modulo
from aula099_package.modulo import soma_do_modulo
from aula099_package.modulo import *

# print(*path, sep='\n')
print(aula099_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(soma_do_modulo(1, 2))
print(variavel)
# print(nova_variavel)
