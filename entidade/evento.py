from entidade.organizador import Organizador

class Evento:
    def __init__(self, nome: str, codigo: int, lotacao_max: int, faixa_etaria: int, open_bar: str):
        self.__nome = nome 
        self.__codigo = codigo
        self.__lotacao_max = lotacao_max
        self.__faixa_etaria = faixa_etaria
        self.__open_bar = open_bar
        self.__participantes = [] 
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def lotacao_max(self):
        return self.__lotacao_max
    
    @property
    def faixa_etaria(self):
        return self.__faixa_etaria
    
    @property
    def open_bar(self):
        return self.__open_bar
    
    @property
    def participantes(self):
        return self.__participantes
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
        
    @lotacao_max.setter
    def lotacao_max(self, lotacao_max: int):
        self.__lotacao_max = lotacao_max
        
    @faixa_etaria.setter
    def faixa_etaria(self, faixa_etaria: int):
        self.__faixa_etaria = faixa_etaria
        
    @open_bar.setter
    def open_bar(self, open_bar: str):
        self.__open_bar = open_bar
        
        
    
    