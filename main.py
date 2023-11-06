from tkinter import *
from tkinter import messagebox

import connect

class app():
    def __init__(self):
        self.janela = Tk()
        self.corfundo = '#696969'

        self.janela['bg'] = self.corfundo

        #titulo
        self.janela.title('Login')

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
        self.passw = Entry(self.janela, show='*')
        self.passw.place(x=75,y=81)


        #BUTTON
        Button(self.janela, command=self.login, text='Entrar', font='calibri', bg='green', fg='white').place(x=100,y=120)

        #BOTÃO SAIR
        Button(self.janela, text='Sair', command=self.janela.destroy, bg='red', fg='white', font='calibri').place(x=108,y=180)
        
        self.janela.mainloop()

    def login(self):
        self.usuario = connect.login.usuario_connect
        self.senha = connect.login.usuario_connect


        self.usr = self.user.get()
        self.pw = self.passw.get()

        self.sesion_usr = False
        self.sesion_pw = False

        try:
            if self.usr == self.usuario:
                self.sesion_usr = True
            if self.pw == self.senha:
                self.sesion_pw = True
            else:
                print('Usuário ou Senha errada')
        except:
            pass

        if self.sesion_usr == True:
            pass
        else:
            messagebox.showinfo(title='Erro', message='Usuário incorreto')

        if self.sesion_pw == True:
            self.janela.destroy()
            self.home()
        else:
            messagebox.showinfo(title='Erro', message='Senha incorreta')


    def home(self):
        self.home = Tk()
        self.home.title('Home')
        self.home.mainloop()




app()
