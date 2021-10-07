from tkinter import Tk, ttk
from Archivo import add_File
import pandas as pd


class Automata:

    def __init__(self):
        file_saves = self.add_FilesW()
        self.analyze_File(file_saves)

    # Abrir la ventana para subir archivo
    def add_FilesW(self):
        self.windows = Tk()
        self.windows.geometry("300x100")
        self.windows.title("Automata Finito")
        self.windows.resizable(0, 0)
        file_save = add_File()
        self.windows.mainloop()
        return file_save

    def analyze_File(self, file_saved):

        data_Saved = list(file_saved)

        # Hace una busqueda de cada caracter
        dat_Q = [s for s in data_Saved if "Q" in s]
        dat_S = [s for s in data_Saved if "S" in s]
        dat_q0 = [s for s in data_Saved if "q_0" in s]
        dat_F = [s for s in data_Saved if "F" in s]
        dat_D = [s for s in data_Saved if "D" in s]

        # convertir a cadenas
        Str_Q = "".join(dat_Q)
        Str_S = "".join(dat_S)
        Str_q0 = "".join(dat_q0)
        Str_F = "".join(dat_F)
        Str_D = "".join(dat_D)

        # Eliminar letras
        dat_Q = Str_Q.replace("Q", "")
        dat_S = Str_S.replace("S", "")
        dat_q0 = Str_q0.replace("q_0", "")
        dat_F = Str_F.replace("F", "")
        dat_D = Str_D.replace("D", "")

        #Convertir de nuevo a lista
        row_Q = dat_Q.split(',')
        row_S = dat_S.split(',')
        row_q0 = dat_q0.split(',')
        row_F = dat_F.split(',')
        row_D = dat_D.split(',')

        print("Q: ", row_Q)
        print("S: ", row_S)
        print("q0:",row_q0)
        print("F: ", row_F)
        print("D: ", row_D)

       


app = Automata()
