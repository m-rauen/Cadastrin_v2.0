import PySimpleGUI as sg

class TelaOrganizador:
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
        elif (values['0']) or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao 
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkBlue7')
        layout = [
            [sg.Text('O R G A N I Z A D O R E S', font=("Verdana", 25))],
            [sg.Text('Escolha uma das ações abaixo: ', font=("Verdana", 15))],
            [sg.Radio('Adicionar organizador', "RD1", key='1')],
            [sg.Radio('Alterar dados de organizador', "RD1", key='2')],
            [sg.Radio('Excluir organizador', "RD1", key='3')],
            [sg.Radio('Listar organizador selecionado', "RD1", key='4')],
            [sg.Radio('Listar todos os organizadores', "RD1", key='5')],
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
                
    def pega_dados_organizador(self, lista_organizadores= []):
        sg.ChangeLookAndFeel('DarkBlue7')
        layout = [
            [sg.Text('* DADOS DO ORGANIZADOR* ', font=("Verdana", 25))],
            [sg.Text('Nome: ', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF: ', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Endereço: ', size=(15, 1)), sg.InputText('', key='endereco')],
            [sg.Text('Idade: ', size=(15, 1)), sg.InputText('', key='idade')],
            [sg.Text('Código: ', size=(15, 1)), sg.InputText('', key='codigo')],
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
                
        while True:
            cpf = values['cpf']
            try:
                if cpf.isnumeric() == False: 
                    raise ValueError
                break 
            except ValueError:
                sg.popup_error('Digite um CPF válido!! \n'
                      'O CPF deve ter, precisamente, 11 caracteres numéricos')
                
        while True:
            endereco = values['endereco']
            try: 
                if endereco.isascii() == False or endereco.isnumeric() == True:
                    raise ValueError
                break
            except ValueError:
                sg.popup_error('Digite um endereço válido!! \n'
                      'O endereço deve conter a rua, o bairro e o número da residência')
                
        while True:
            idade = values['idade']
            try: 
                if idade.isnumeric() == False:
                    raise ValueError
                break
            except ValueError:
                sg.popup_error('Digite uma idade válida!! \n'
                      'Idades devem conter somente o número')
        
        #LEMBRAR: adicionar no controlador_participante o tratamento para codigos repetidos!!        
        while True:
            codigo_org = values['codigo']
            try: 
                if codigo_org.isnumeric() == False:
                    raise ValueError
                break 
            except ValueError:
                print('Digite um código válido!! \n'
                      'Os códigos devem conter SOMENTE números')
                
        self.close()
        return {"nome":nome, "cpf":cpf, "endereco":endereco, "idade":idade, "codigo":codigo_org}

    def mostra_organizador(self, dados_organizador):
        string_org = ""
        for org in dados_organizador:
            string_org = string_org + "Nome: " + org["nome"] + '\n'
            string_org = string_org + "CPF: " + org["cpf"] + '\n'
            string_org = string_org + "Endereço: " + org["endereco"] + '\n'
            string_org = string_org + "Idade: " + org["idade"] + '\n' 
            string_org = string_org + "Código: " + org["codigo"] + '\n'
        
        sg.popup('ORGANIZADORES:', string_org)
        
    #LEMBRAR: checar se essa parte do código ainda se faz necessária, dada a nova func "seleciona_[...]" 
    #LEMBRAR: caso ainda seja válida essa func, fazer tratamento de erros com o "popup_error"
    def pega_organizador_codigo(self):
        codigo = input('Código do organizador: ')
        try:
            if codigo.isnumeric() == False: 
                raise ValueError
        except ValueError:
            print('Digite um código válido!! \n'
                      'Os códigos devem conter SOMENTE números')
    
    def seleciona_organizador(self):
        sg.ChangeLookAndFeel('DarkBlue7')
        layout = [
            [sg.Text('# SELEÇÃO DE ORGANIZADOR #', font=("Verdana", 25))],
            [sg.Text('Código: ', size=(15,1)), sg.InputText('', 'codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastrin - v2.0').Layout(layout)
        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo
    
    def mostra_mensagem(self, msg: str):
        sg.popup("", msg)
        
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()