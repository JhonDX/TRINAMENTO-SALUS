from tkinter import *
from tkinter import messagebox
from ldap3 import Server, Connection, SAFE_SYNC



class log():
    def __init__(self):
        self.janela = Tk()
        self.corfundo = '#696969'
        self.version ='V 0.1'
        self.janela['bg'] = self.corfundo

        #titulo
        self.janela.title('Login')
        #version
        Label(self.janela, text=self.version, bg=self.corfundo).place(x=220,y=230)

        #ESQUECI O NOME DESSA PORRA!!!
        self.janela.resizable(False, False)

        #DIÂMETRO
        self.janela.geometry('250x250')

        #USAURIO
        Label(self.janela, text='Usuário :', font='calibri', bg=self.corfundo).place(x=10,y=30)
        self.user = Entry(self.janela)
        self.user.place(x=75,y=31)

        #SENHA
        Label(self.janela, text='  Senha  :', font='calibri', bg=self.corfundo).place(x=10,y=80)
        self.password = Entry(self.janela, show='*')
        self.password.place(x=75,y=81)


        #BUTTON
        Button(self.janela, command=self.login, text='Entrar', font='calibri', bg='green', fg='white').place(x=100,y=120)

        #BOTÃO SAIR
        Button(self.janela, text='Sair', command=self.janela.destroy, bg='red', fg='white', font='calibri').place(x=108,y=180)

        self.janela.mainloop()

    def login(self):
        self.usuario = self.user.get()
        self.senha = self.password.get()
        self.dom = 'gacc'
        server = Server('192.168.0.1')
        log = False
        try:
            conn = Connection(server, f'{self.dom}\\{self.usuario}', f'{self.senha}', client_strategy=SAFE_SYNC, auto_bind=True)
            status, result, response, _ = conn.search('o=test','(objectclass=*)')
            log = True
            import app


        except:
            messagebox.showinfo(title='Erro', message='Usuário ou Senha incorretos')

        if log == True:
            app.home()
        else:
            pass

    def fechar(self):
        self.janela.destroy()


log()
