#Principio Solid(O) Aberto e Fechado:
#Entradas diferentes geram ações diferentes
"""
class Circo:
    def apresentar(self, tipo):
        if tipo ==1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self):
        print('Malabarista apresentando seu show')
    
    def apresentar_palhaco(self):
        print('Palhaço apresentando seu show')


#Essa classe está definida com uma ideia de fechada
#É definida por tipo um e tipo dois, não conseguirei adicionar outro tipo
#Se quiser adicionar outro tipo irá alterar o código já existente

circo = Circo()
circo.apresentar(1)
"""
#O módulo será aberto se ainda estiver disponível para extensão
#Veja:
class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

class Malabarista:
    def apresentar_show(self):
        print('Malabarista apresentando seu show')

class Palhaco:
    def apresentar_show(self):
        print('Palhaço apresentando seu show')

#Adicionando classe domador
class Domador:
    def apresentar_show(self):
        print('Domador apresentando seu show')

"""
Perceba que a classe circo só foi feita para apresentar o show
Foram criadas outras classes para quem irá apresentar
A classe circo está fechada para alterações, mas aberta para extensões
"""

circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)

#Se eu quiser, posso adicionar uma classe Domador para apresentar seu show
domador = Domador()
circo.apresentar(domador)

#A fragilidade é ter que criar novas classes para adicionar novos apresentadores