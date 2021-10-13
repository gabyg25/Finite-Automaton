from tkinter import Tk, ttk, messagebox
from Archivo import *

class Automata:

    def __init__(self):
        self.windows = Tk()
        self.windows.geometry("300x150")
        self.windows.title("Automata Finito")
        self.windows.resizable(0, 0)
        data = add_File()
        if data is True:
            self.main_Interface()
        else:
            messagebox.showerror("Error", "No Cargo Ningún Archivo")
            self.windows.destroy()
        self.windows.mainloop()
 
    def main_Interface(self):
        self.windows.destroy()
        main_windows = Tk()
        main_windows.geometry("300x200")
        main_windows.title("AFN/AFD/")
        main_windows.resizable(0,0)

        ttk.Label(main_windows, text="A U T O M A T A ~ F I N I T O").place(relx=0.25,rely=0.10)
        ttk.Label(main_windows,text="Cadena: ").place(relx=0.15,rely=0.35)
        add_String = ttk.Entry(main_windows)
        add_String.place(relx=0.35,rely=0.35)
        Btn_Review = ttk.Button(main_windows, text="Evaluar Cadena",command=lambda:self.analyze_File())
        Btn_Review.place(relx=0.35, rely=0.55)
        main_windows.mainloop()
    
    def analyze_File(self):

        states = send_States()
        alphabet = send_Alphabet()
        initial = send_InitialState()
        final = send_FinalState()
        trans = send_Transitions()

        print("Q: ",states)
        print("S:", alphabet)
        print("q0:", initial)
        print("F", final)
        print("D:", trans)

Automata()
