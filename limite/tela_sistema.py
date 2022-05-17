import PySimpleGUI as sg

class TelaSistema():
    def __init__(self):
        self.__window = None
        self.init_components()
        
    def close(self):
        self.__window.Close()
    
    def init_components(self):
        sg.ChangeLookAndFeel('DarkBlue7')
        layout = [
            [sg.Text('C A D A S T R I N', font=("Verdana", 25))],
            [sg.Text('Bem vindo ao sistema de controle para festas!', font=("Verdana", 12), background_color="Grey")],
            [sg.Text('Por favor, escolha um dos menus abaixo:', font=("Verdana",15))],
            [sg.Radio('Participantes', "RD1", key='1')],
            [sg.Radio('Organizadores', "RD1", key='2')],
            [sg.Radio('Eventos', "RD1", key='3')],
            [sg.Radio('Fechar Sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastrin - v2.0').Layout(layout)
        
    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0 
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif (values['0']) or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    