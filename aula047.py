"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para 
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na 
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# Minha solução:
# palavra_secreta = 'uva'
# tentativas = 0
# letras_certas = ''

# print('Palavra secreta: ' + '*' * len(palavra_secreta))

# while True:
#     if len(palavra_secreta) == len(letras_certas):
#         break

#     letra_sugerida = input('\n\nDigite uma letra: ')

#     if len(letra_sugerida) != 1:
#         print('Digite apenas uma letra')
#         continue
#     else:
#         tentativas += 1

#     if letra_sugerida in palavra_secreta:
#         letras_certas += letra_sugerida
    
#         for letra in palavra_secreta:
#             if letra in letras_certas:
#                 print(letra, end='')
#             else:
#                 print('*', end='')

# print(f'\n\nVocê acertou com {tentativas} tentativas.')

# Solução:
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
