"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> entregue-me o próximo valor
iter -> entregue-me seu iterador
"""
# texto = 'Julio'.__iter__()
# texto = iter('Julio') # __iter__()

# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(next(texto)) # __next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

texto = 'Julio' # Iterável
# iterador = iter(texto) # Iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
