#Solid(L): Principio de Substituição de Liskov

#Para o mesmo método, o comportamento foi diferente entre as heranças
#Essa é a quebra do principio de liskov
class PessoaA:

    def se_apresentar(self):
        print('Olá! Sou a pessoa A')

class PessoaB(PessoaA):

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print('Estou alterando esse método')

pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()

"""
Basicamente o principio de liskov diz que se temos um objeto 1
e um objeto 2 a gente precisa ter a mesma funcionalidade para o mesmo método
"""

#Exemplo de aplicação Principio de Liskov

from typing import Type

class Animal:
    def comer(self):
        print('O animal está comendo')

    def dormir(self):
        print('O animal está dormindo')

    def andar(self):
        print('O animal está andando na jaula')

class Aves(Animal):

    def __init__(self):
        super().__init__()

    def cantar(self):
        print('A ave está cantando')

class Pinguim(Aves):

    def __init__(self):
        super().__init__()

    def escorregar(self):
        print('O pinguim esta escorregando no gelo')

class Pessoa:

    def observar(self, animal: Type[Animal]):
        animal.comer()

#Eu posso pegar uma subclasse que esteja na mesma arvore de heranças e utilizar os mesmos métodos

#Dica, tenta fazer o elemento mais generico pra cima e ir especificando conforme vamos descendo a arvore