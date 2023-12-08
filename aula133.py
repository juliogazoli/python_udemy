"""
Encapsulamento (modificadores de acesso: public, protected, private)
Python NÃO TEM modificadores de acesso
Mas podemos seguir as seguintes convenções
    (sem underline) = public
        pode ser usado em qualquer lugar
_   (um underline) = protected
        não deve ser usado fora da classe
        ou suas subclasses
__  (dois underlines) = private
        "name mangling" (desfiguração de nomes) em Python
        só deve ser usado na classe que foi
        declarado
"""


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        return 'metodo_publico'

    def _metodo_protegido(self):
        return 'metodo_protegido'

    def __metodo_privado(self):
        return 'metodo_privado'


f = Foo()

print(f.public)
print(f.metodo_publico())

print(f._protected)
print(f._metodo_protegido())

print(f._Foo__private)
print(f._Foo__metodo_privado())
