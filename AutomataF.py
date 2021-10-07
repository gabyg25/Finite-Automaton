from tkinter import Tk, ttk
from Archivo import add_File

class Automata: 
    
    def __init__(self):
        self.add_FilesW()

    #Abrir la ventana para subir archivo
    def add_FilesW(self):
        self.windows = Tk()
        self.windows.geometry("300x100")
        self.windows.title("Automata Finito")
        self.windows.resizable(0,0)

        btn_File = ttk.Button(self.windows, text="Add File", command=lambda: add_File())
        btn_File.place(relx=0.36, rely=0.30)

        self.windows.mainloop()

app = Automata()