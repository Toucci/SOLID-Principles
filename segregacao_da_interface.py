#Solid(I): Principio da Segregação da Interface

"""
Evitar depender de coisas que não utilizamos

"""

from abc import ABC, abstractmethod

class Ave(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should Implement comer method'

    @abstractmethod
    def voar(self):
        raise 'Should Implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should Implement gritar method'

class Canario(Ave):

    def comer(self):
        print('Estou comendo!')

    def voar(self):
        print('Estou voando!')

    def gritar(self):
        print('Estou gritando!')

class Pinguim(Ave):

    def comer(self):
        print('Estou comendo!')

    def voar(self):
        None

    def gritar(self):
        print('Estou gritando!')

#Perceba que o pinguim não voa, mas foi obrigado a utilizar esse método
#Utilização do principio de segregação da interface:

class Ave_que_voa(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should Implement comer method'

    @abstractmethod
    def voar(self):
        raise 'Should Implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should Implement gritar method'

class Ave_que_nao_voa(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should Implement comer method'

    @abstractmethod
    def gritar(self):
        raise 'Should Implement gritar method'

#Perceba que agora não estou generalizando todos os comportamentos em si

class Canario(Ave_que_voa):

    def comer(self):
        print('Estou comendo!')

    def voar(self):
        print('Estou voando!')

    def gritar(self):
        print('Estou gritando!')

class Pinguim(Ave_que_nao_voa):

    def comer(self):
        print('Estou comendo!')

    def gritar(self):
        print('Estou gritando!')