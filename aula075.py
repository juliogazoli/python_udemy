"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""

# # Minha solução
# def duplica(numero):
#     return numero * 2


# def triplica(numero):
#     return numero * 3


# def quadruplica(numero):
#     return numero * 4


# print(duplica(2))
# print(duplica(3))
# print(duplica(4))


# Solução
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadruplica = criar_multiplicador(4)

print(duplica(2))
print(triplica(2))
print(quadruplica(2))