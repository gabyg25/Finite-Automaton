from os import read
from tkinter import filedialog

#Agregar el archivo de texto
def add_File():
    new_File = filedialog.askopenfilename(title="Add File", initialdir="c:/desktop", filetypes=(("txt files","*.txt"),("todos los archivos","*.*")))
    if new_File != '':
        file_Automaton = open(new_File,"r")
        new_text = file_Automaton.read()
        file_Automaton.close()
        print(new_text)
    return new_text
