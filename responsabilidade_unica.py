#uma classe só deve ser um e somente um motivo para mudar
#God class não é uma boa prática

#Solid(S) - Responsabilidade única é basicamente dividir as funcionalidades de seu módulo

#Exemplo:

class SistemaCadastral:
    def cadastrar(self,nome: str,idade : int) -> None:
        if isinstance(nome, str) and (idade, int):
            print('Acessando o banco de dados...')
            print(f'Cadastrar Usuário {nome}, Idade {idade}')
        else:
            print('Dados inválidos!')

#Perceba que nesta classe acima o método cadastrar possui muitas funcionalidades que fogem do escopo
#Como por exemplo verificar se o usuário atende a tipagem, mostrar o cadastro e retornar erro caso as informações sejam inválidas.

#Com o principio da responsabilidade única, podemos quebrar essas funcionalidades em mais métodos.
#Veja:
class SistemaCadastral:
    def cadastrar(self,nome: str, idade: int) -> None:
        if self.__verificar_validade_dos_dados(nome, idade):
            self.__cadastrar_usuario(nome,idade)
        else:
            self.__dados_errados(nome_idade)

    def __verificar_validade_dos_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else
            return False
    
    def __cadastrar_usuario(self, nome: str, idade: int):
        print('Acessando o banco de dados...')
        print(f'Cadastrar Usuário {nome}, Idade {idade}')

    def __dados_errados(self, nome: str, idade: int):
        print('Dados inválidos!')

#Perceba que separamos todas as funcionalidades do método cadastrar em métodos privados, e adicionamos suas funcionalidades na cadastrar
#Assim fica mais distribuído, além de se necessitar de alguma alteração, ela será feita
#nos próprios métodos privados, e não na classe cadastrar.
