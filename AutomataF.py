from tkinter import Tk, ttk
from Archivo import add_File
import pandas as pd

class Automata: 
    
    def __init__(self):
        file_saves = self.add_FilesW()
        self.analyze_File(file_saves)

    #Abrir la ventana para subir archivo
    def add_FilesW(self):
        self.windows = Tk()
        self.windows.geometry("300x100")
        self.windows.title("Automata Finito")
        self.windows.resizable(0,0)
        file_save = add_File()
        self.windows.mainloop()
        return file_save
    
    def analyze_File(self,file_saved):
        
        data_Saved = list(file_saved)

        #Hace una busqueda de cada caracter 
        dat_Q = [s for s in data_Saved if "Q" in s]
        dat_S = [s for s in data_Saved if "S" in s]
        dat_q0 = [s for s in data_Saved if "q0" in s]
        dat_F = [s for s in data_Saved if "F" in s]
        dat_D = [s for s in data_Saved if "D" in s]

        #convertir a cadenas
        Str_Q = "".join(dat_Q)
        Str_S = "".join(dat_S)
        Str_q0 = "".join(dat_q0)
        Str_F = "".join(dat_F)
        Str_D = "".join(dat_D)

        #Convertir a listas
        row_Q = list(Str_Q)
        row_S = list(Str_S)
        row_q0 = list(Str_q0)
        row_F = list(Str_F)
        row_D = list(Str_D)

        # Eliminar Letras
        row_Q.pop(0)
        row_S.pop(0)
        row_q0.pop(0)
        row_F.pop(0)
        row_D.pop(0)
       
        print("Nueva Q: ", row_Q)
        print("Nueva S: ", row_S)
        print("Nueva q0: ", row_q0)
        print("Nueva F: ", row_F)
        print("Nueva D: ", "".join(row_D))

      
app = Automata()