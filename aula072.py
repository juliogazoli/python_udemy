# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Minha solução:
# def multiplica(*args):
#     produto = 1
#     for numero in args:
#         produto *= numero
#     return produto


# total = multiplica(2, 3, 4)
# print(total)

# Solução:
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)


# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# Minha solução:
# def par_ou_impar(numero):
#     if numero % 2 == 0:
#         return 'Par'
#     else:
#         return 'Ímpar'


# r_1 = par_ou_impar(1)
# print(r_1)

# r_2 = par_ou_impar(2)
# print(r_2)

# Solução:
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'

    return f'{numero} é ímpar'


print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))
