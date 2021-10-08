from tkinter import Tk, ttk
from Archivo import add_File
import pandas as pd


class Automata:

    def __init__(self):
        self.add_FilesW()

    # Abrir la ventana para subir archivo
    def add_FilesW(self):
        self.windows = Tk()
        self.windows.geometry("300x100")
        self.windows.title("Automata Finito")
        self.windows.resizable(0, 0)
        file_save = add_File()
        self.analyze_File(file_save)

        self.windows.mainloop()
        

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
        
        # row_D2 = [row_D[i:i + 3] for i in range(0, len(row_D), 3)]

        print("Q: ", row_Q)
        print("S: ", row_S)
        print("q0:",row_q0)
        print("F: ", row_F)
        print("D: ", row_D)

        self.windows.destroy()
        # self.main_Interface(row_Q, row_S, row_q0, row_F, row_D2)

    def main_Interface(self, Q, S, q_0, F, D):
        main_windows = Tk()
        main_windows.geometry("300x200")
        main_windows.title("AFN/AFD/")
        main_windows.resizable(0,0)

        ttk.Label(main_windows, text="A U T O M A T A ~ F I N I T O").place(relx=0.25,rely=0.10)
        ttk.Label(main_windows,text="Cadena: ").place(relx=0.15,rely=0.35)
        add_String = ttk.Entry(main_windows)
        add_String.place(relx=0.35,rely=0.35)
        Btn_Review = ttk.Button(main_windows, text="Evaluar Cadena",command=lambda:"#")
        Btn_Review.place(relx=0.35, rely=0.55)
        main_windows.mainloop()
    
    


app = Automata()
