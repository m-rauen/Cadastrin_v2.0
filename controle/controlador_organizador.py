from entidade.organizador import Organizador 
from limite.tela_organizador import TelaOrganizador

class ControladorOrganizador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_organizador = TelaOrganizador()
        self.__organizadores = []
        
    @property
    def organizadores(self):
        return self.__organizadores
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_organizador, 2: self.altera_organizador, 3: self.exclui_organizador, 4: self.lista_um_organizador, 5: self.lista_organizadores, 0: self.voltar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_organizador.tela_opcoes()]()
    
    def pega_organizador_codigo(self, codigo_org):
        for organizer in self.__organizadores:
            if (organizer.codigo == codigo_org):
                return organizer
        return None
        
    def inclui_organizador(self):
        dados_organizador = self.__tela_organizador.pega_dados_organizador()
        organizador = Organizador(dados_organizador["nome"], dados_organizador["cpf"], dados_organizador["endereco"], dados_organizador["idade"], dados_organizador["codigo"])
        self.__organizadores.append(organizador)
        
    def exclui_organizador(self):
        self.lista_organizadores
        if len(self.__organizadores) < 1:
            pass
        else:
            codigo_organizador = self.__tela_organizador.seleciona_organizador()
            organizador = self.pega_organizador_codigo(codigo_organizador)
            if organizador is not None:
                self.__organizadores.remove(organizador)
                self.__tela_organizador.mostra_mensagem('Organizador excluído com sucesso!')
            else:
                self.__tela_organizador.mostra_mensagem('Organizador inexiste!')
                
    def altera_organizador(self):
        self.__tela_organizador.mostra_mensagem('* ALTERANDO ORGANIZADOR *')
        if len(self.__organizadores) < 1: 
            pass
        else: 
            codigo_organizador = self.__tela_organizador.seleciona_organizador()
            organizador = self.pega_organizador_codigo(codigo_organizador)
            if organizador is not None:
                novo_organizador = self.__tela_organizador.pega_dados_organizador()
                organizador.nome = novo_organizador["nome"]
                organizador.cpf = novo_organizador["cpf"]
                organizador.endereco = novo_organizador["endereco"]
                organizador.idade = novo_organizador["idade"]
                organizador.codigo = novo_organizador["codigo"]
                self.lista_organizadores()
            else: 
                self.__tela_organizador.mostra_mensagem('Organizador inexistente!')
        
    def lista_um_organizador(self):
        if len(self.__organizadores) < 1: 
            self.__tela_organizador.mostra_mensagem('Não foram cadastrados organizadores até o momento!')
        else: 
            codigo_organizador = self.__tela_organizador.seleciona_organizador()
            organizador = self.__tela_organizador.pega_organizador_codigo(codigo_organizador)
            if organizador is not None: 
                self.__tela_organizador.mostra_organizador({"nome":organizador.nome, "cpf":organizador.cpf, "endereco":organizador.endereco, "idade":organizador.idade, "codigo":organizador.codigo})
            else:
                self.__tela_organizador.mostra_organizador('Organizador inexistente!')
                
    def lista_organizadores(self):
        if len(self.__organizadores) < 1: 
            self.__tela_organizador.mostra_mensagem('Não foram cadastrados organizadores até o momento!')
        else: 
            dados_do_org = []
            for organizador in self.__organizadores:
                dados_do_org.append({"nome":organizador.nome, "cpf":organizador.cpf, "endereco":organizador.endereco, "idade":organizador.idade, "codigo":organizador.codigo})
            self.__tela_organizador.mostra_organizador(dados_do_org)
                
    def voltar(self):
        self.__controlador_sistema.abre_tela()
        
    
   
        
    
     

