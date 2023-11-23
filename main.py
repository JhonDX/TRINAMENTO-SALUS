from tkinter import *
from tkinter import messagebox

class home():
        def __init__(self):
                import connect
                connect.log.fechar()
                self.home = Tk()
                self.home.title('Home')
                self.home.resizable(False, False)
                self.home.geometry('500x500')
                self.home.mainloop()

home()
