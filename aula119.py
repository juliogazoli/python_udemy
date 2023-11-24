"""
Exercício - Lista de tarefas com desfazer e refazer
Música para codar =)
Everybody wants to rule the world - Tears for fears
todo = [] -> Lista de tarefas
todo = ['fazer café'] -> Adicionar fazer café
todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
desfazer = ['fazer café',] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
"""

# Minha Solução:
import os

todo = []
refazer = []


def imprime_tarefas():
    print()
    print('TAREFAS:')
    for tarefa in todo:
        print(tarefa)
    print()


while True:
    print('Comandos: listar, desfazer, refazer')
    resposta = input('Digite uma tarefa ou comando: ')
    resposta_formatada = resposta.lower().strip()

    if resposta_formatada == 'listar':
        imprime_tarefas()

    elif resposta_formatada == 'desfazer':
        if not todo:
            print()
            print('Nada a desfazer')
        else:
            refazer.append(todo.pop())
        imprime_tarefas()

    elif resposta_formatada == 'refazer':
        if not refazer:
            print()
            print('Nada a refazer')
        else:
            todo.append(refazer.pop())
        imprime_tarefas()

    elif resposta_formatada == 'clear':
        os.system('clear')

    else:
        todo.append(resposta_formatada)
        imprime_tarefas()
