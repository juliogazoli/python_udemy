"""
Exercício - sistema de perguntas e respostas
"""

# Minha solução
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
contador = 0
for pergunta in perguntas:
    print(f'Pergunta: {pergunta["Pergunta"]}\n')
    print('Opções:')
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcao}')
    resposta_usuario = int(input('Escolha uma opção: '))
    resposta_correta = pergunta['Opções'].index(pergunta['Resposta'])
    if resposta_correta == resposta_usuario:
        print('Acertou\n')
        acertos += 1
    else:
        print('Errou\n')
    contador += 1
print(f'Você acertou {acertos} de {contador} perguntas.')
