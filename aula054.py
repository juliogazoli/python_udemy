"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar os valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

# Minha Solução:
# lista_de_compras = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

#     if opcao == 'i':
#         valor = input('Valor: ')
#         lista_de_compras.append(valor)
    
#     if opcao == 'a':
#         try:
#             indice_apagar = int(input('Escolha o índice para apagar: '))
#             del(lista_de_compras[indice_apagar])
#         except:
#             print('Não foi possível apagar este índice')

#     if opcao == 'l':
#         if len(lista_de_compras) == 0:
#             print('Nada para listar')
#         for indice, item in enumerate(lista_de_compras):
#             print(indice, item)


# Solução:
import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erros desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')