from controle.controlador_eventos import ControladorEventos
from controle.controlador_participante import ControladorParticipante
from controle.controlador_organizador import ControladorOrganizador
from limite.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_eventos = ControladorEventos(self)
        self.__controlador_participante = ControladorParticipante(self) 
        self.__controlador_organizador = ControladorOrganizador(self)
        self.__tela_sistema = TelaSistema()
        
    @property
    def controlador_eventos(self):
        return self.__controlador_eventos
    
    @property
    def controlador_participante(self):
        return self.__controlador_participante 
    
    @property
    def controlador_organizador(self):
        return self.__controlador_organizador
    
    #Chama o controlador_eventos na tela
    def tela_eventos(self):
        self.__controlador_eventos.abre_tela()
    
    #Chama o controlador_participante na tela
    def tela_participante(self):
        self.__controlador_participante.abre_tela()
        
    #Chama o controlador_organizador na tela
    def tela_organizador(self):
        self.__controlador_organizador.abre_tela()
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        lista_opcoes = {1: self.tela_participante, 2: self.tela_organizador, 3: self.tela_eventos, 0: self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
    
    
    