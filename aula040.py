""" Calculadora com while """

# Minha solução
# while True:

#     num1 = input('Digite um número: ')
    
#     if num1.isdigit():
#        num1_int = int(num1)
#     else:
#         continue

#     num2 = input('Digite outro número: ')

#     if num2.isdigit():
#         num2_int = int(num2)
#     else:
#         continue

#     operacao = input('Digite uma operação [+ - / *]: ')

#     if operacao == '+':
#         resultado = num1_int + num2_int
#     elif operacao == '-':
#         resultado = num1_int - num2_int
#     elif operacao == '/':
#         resultado = num1_int / num2_int
#     elif operacao == '*':
#         resultado = num1_int * num2_int
#     else:
#         print('Operação inválida')
#         continue

#     print(f'{num1_int} {operacao} {num2_int} = {resultado}')

#     resp = input('Deseja sair? [S]im: ')

#     if resp.lower() == 's':
#         break

# Solução
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
