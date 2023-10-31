"""
Exemplo de uso dos sets
"""

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letra:
        print('PARABÉNS')
        break

    print(letras)
