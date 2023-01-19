"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade
de caracteres da string
"""

variavel = 'Olá mundo'
print(variavel[5])
print(variavel[-4])
print(variavel[4:])
print(variavel[4:8])
print(variavel[:5])
print(variavel[-8:-2])

print(len(variavel))
print(len(variavel[3]))

print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):2])
print(variavel[0:9:2])
print(variavel[::2])
print(variavel[::-1])
print(variavel[-1:-10:-1])
