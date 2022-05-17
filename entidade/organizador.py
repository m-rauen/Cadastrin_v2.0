from entidade.usuario import Usuario 

class Organizador(Usuario):
    def __init__(self, nome: Usuario, cpf: Usuario, endereco: Usuario, idade: Usuario, codigo: int): 
        super().__init__(nome, cpf, endereco, idade)
        self.__codigo = codigo
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
        
    
    