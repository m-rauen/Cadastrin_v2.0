from curses.ascii import US
from entidade.usuario import Usuario

class Participante(Usuario):
    def __init__(self, nome: Usuario, cpf: Usuario, endereco: Usuario, idade: Usuario, vacina_3d: str, exame_pcr: str, codigo: int):
        super().__init__(nome, cpf, endereco, idade)
        self.__vacina_3d = vacina_3d
        self.__exame_pcr = exame_pcr
        self.__codigo = codigo
        
    @property
    def vacina_3d(self):
        return self.__vacina_3d
    
    @property
    def exame_pcr(self):
        return self.__exame_pcr
    
    @property
    def codigo(self):
        return self.__codigo
    
    @vacina_3d.setter
    def vacina_3d(self, vacina_3d: str):
        self.__vacina_3d = vacina_3d
        
    @exame_pcr.setter
    def exame_pcr(self, exame_pcr: str):
        self.__exame_pcr = exame_pcr
        
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
        
    
        
    

