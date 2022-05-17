from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome: str, cpf: int, endereco: str, idade: int):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__idade = idade 
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        
    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf
        
    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco
        
    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade 
    