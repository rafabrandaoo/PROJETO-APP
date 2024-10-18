import database
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    def controla_digitacao_user(self, instance):
        caracteres_validos = 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        instance.text = ''.join(c for c in instance.text if c in caracteres_validos and c != ' ')
            
    def Cadastrar(self):
        result = database.verifica_existencia_user(self.ids.user.text)

        if result:
            self.ids.usuario_status.text = 'Usuário já cadastrado'
        else: 
            if len(self.ids.senha.text) >= 1:
                database.cadastra_user_no_banco(self.ids.user.text, self.ids.senha.text)
                self.ids.usuario_status.text = 'USUARIO NOVO CADASTRADO'
            else:
                self.ids.usuario_status.text = 'DIGITE UMA SENHA VALIDA'
    

    def Acessar(self):
        result = database.verifica_user_senha(self.ids.user.text, self.ids.senha.text)
        if result:
            self.ids.usuario_status.text = 'SISTEMA ACESSADO'
        else:
            self.ids.usuario_status.text = 'ACESSO NEGADO'

class mainApp(App):
    def build(self):
        return MyBoxLayout()

database.connect_db()
database.create_table()
mainApp().run()
