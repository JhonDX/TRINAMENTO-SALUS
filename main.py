from tkinter import *



class app():
    def __init__(self):
        self.janela = Tk()

        #titulo
        self.janela.title('Login')

        #ESQUECI O NOME DESSA PORRA!!!
        self.janela.resizable(False, False)

        #DIÂMETRO
        self.janela.geometry('250x250')

        #USAURIO
        Label(self.janela, text='Usuário :').grid(row=1,column=1)

        Entry(self.janela, show='*').grid(row=1,column=2)

        #BOTÃO SAIR
        Button(self.janela, text='Sair', command=self.janela.destroy).grid(row=0, column=0)


        self.janela.mainloop()

app()