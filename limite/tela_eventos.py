import PySimpleGUI as sg

class TelaEventos:
    def __init__(self):
        self.__window = None 
        self.init_opcoes() 
        
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
        elif values['6']:
            opcao = 6
        elif (values['0']) or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao 
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkBlue7')
        layout = [
            [sg.Text('E V E N T O S', font=("Verdana", 25))],
            [sg.Text('Escolha uma das ações abaixo: ', font=("Verdana", 15))],
            [sg.Radio('Adicionar evento', "RD1", key='1')],
            [sg.Radio('Alterar dados do evento', "RD1", key='2')],
            [sg.Radio('Excluir evento', "RD1", key='3')],
            [sg.Radio('Mostrar evento', "RD1", key='4')],
            [sg.Radio('Listar todos os eventos', "RD1", key='5')],
            [sg.Radio('Adicionar participante no evento', "RD1", key='6')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastrin - v2.0').Layout(layout)
    
    def trata_opçoes(self, msg: str = '', inteiros_validos = []):
        valor = input(msg)
        try:
            inteiro = int(valor)
            if inteiros_validos and inteiro not in inteiros_validos:
                raise ValueError
            return inteiro
        except ValueError:
            print('Valor inválido!!\n'
                  'Por favor, digite novamente.')
            if inteiros_validos:
                print('Valores aceitos: {}'.format(inteiros_validos))
            
    def pega_dados_evento(self, lista_eventos = []):
        sg.ChangeLookAndFeel('DarkBlue7')
        layout = [
            [sg.Text('* DADOS DO EVENTO * ', font=("Verdana", 25))],
            [sg.Text('Nome: ', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Código: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Lotação Máxima: ', size=(15, 1)), sg.InputText('', key='lotacao_max')],
            [sg.Text('Faixa Etária: ', size=(15, 1)), sg.InputText('', key='faixa_etaria')],
            [sg.Text('Open Bar: ', size=(15, 1)), sg.InputText('', key='open_bar')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastrin - v2.0').Layout(layout)
        button, values = self.open()
        while True:
            nome = values['nome']           
            try:
                if nome.isascii() == False or nome.isnumeric == True:
                    raise ValueError
                if len(nome) < 1:
                    raise ValueError
                break
            except ValueError:
                sg.popup_error('Digite um nome válido!! \n'
                      'O nome deve ter, no mínimo, 1 carácter; \n'
                      'O nome não pode ser composto SOMENTE por números')
        
        #LEMBRAR: adicionar no controlador_participante o tratamento para codigos repetidos!!         
        while True:
            codigo = values['codigo']
            try:
                if codigo.isnumeric() == False:
                    raise ValueError
                break 
            except ValueError:
                sg.popup_error('Digite um código válido!! \n'
                          'Os códigos devem conter SOMENTE números')
                
        while True:
            lotacao_max = values['lotacao_max']
            try:
                if lotacao_max .isnumeric() == False:
                    raise ValueError
                break
            except ValueError:
                sg.popup_error('Digita uma lotação válida!! \n'
                          'As lotações máximas devem ser SOMENTE o número máximo que a casa permite')
                    
        while True:
            faixa_etaria = values['faixa_etaria']
            try:
                if faixa_etaria.isnumeric() == False:
                    raise ValueError
                break
            except ValueError:
                sg.popup_error('Digite uma faixa etária válida!! \n'
                            'A faixa etária deve ser SOMENTE a idade mínima para entrar')
                    
        while True:
            open_bar = values['open_bar']
            try: 
                if open_bar.isnumeric() == True:
                    raise ValueError
                break
            except ValueError:
                sg.popup_error('Digite uma resposta válida!! \n'
                          "A opção correspondente deve ser 'S' (sim) ou 'N' (não)")
        
        self.close()        
        return {"nome":nome, "codigo":codigo, "lotacao_max":lotacao_max , "faixa_etaria":faixa_etaria, "open_bar":open_bar}
        
    def mostra_evento(self, dados_evento):
        string_evento = ""
        for evnt in dados_evento:
            string_evento = string_evento + "Nome: " + evnt["nome"] + '\n'
            string_evento = string_evento + "Código: " + evnt["codigo"] + '\n'
            string_evento = string_evento + "Lotação Máxima: " + evnt["lotacao_max"] + '\n'
            string_evento = string_evento + "Faixa Etária: " + evnt["faixa_etaria"] + '\n' 
            string_evento = string_evento + "Open Bar: " + evnt["open_bar"] + '\n'
            
        sg.popup('EVENTOS:', string_evento)
            
    def seleciona_evento(self):
        sg.ChangeLookAndFeel('DarkBlue7')
        layout = [
            [sg.Text('# SELEÇÃO DE EVENTO #', font=("Verdana", 25))],
            [sg.Text('Código: ', size=(15,1)), sg.InputText('', 'codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastrin - v2.0').Layout(layout)
        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo 
    
    #LEMBRAR: checar se essa parte do código ainda se faz necessária, dada a nova func "seleciona_[...]" 
    #LEMBRAR: caso ainda seja válida essa func, fazer tratamento de erros com o "popup_error"    
    def pega_evento_codigo(self):
        codigo = input('Código do evento: ')
        try:
            if codigo.isnumeric() == False: 
                raise ValueError
        except ValueError:
            print('Digite um código válido!! \n'
                      'Os códigos devem conter SOMENTE números')
                
    def mostra_mensagem(self, msg: str):
        sg.popup("", msg) 
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
    
            
        
    
    