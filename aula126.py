"""
__dict__ e vars para atributos de instância
"""


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


# p1 = Pessoa('João', 35)
# # p1.nome = 'EITA'
# # print(p1.nome)
# # del p1.nome
# # print(p1.idade)

# # print(p1.__dict__)

# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)

dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

print(vars(p1))
