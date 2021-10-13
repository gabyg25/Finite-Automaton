import os
from tkinter import filedialog, messagebox

# Agregar el archivo de texto
def add_File():
    states_File = False
    new_File = filedialog.askopenfilename(
        title="Add File", initialdir="c:/desktop", filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
    if new_File != '':
        new_extension = os.path.splitext(new_File)
        if new_extension[1] == ".txt":
            with open(new_File) as n_files:
                lines_saved = n_files.readlines()
                for read_Lines in lines_saved:
                    read_Lines = read_Lines.replace("{", '').replace("}",'')
                    read_Lines = read_Lines.replace("\t", '')
                    if read_Lines[0] == 'Q':
                        read_Lines = read_Lines.replace("Q=", '').replace("\n",'')
                        add_States(read_Lines)
                    if read_Lines[0] == 'S':
                        read_Lines = read_Lines.replace("S=", '').replace("\n",'')
                        add_Alphabet(read_Lines)
                    if read_Lines[0] == 'q':
                        read_Lines = read_Lines.replace("q0=", '').replace("\n",'')
                        add_InitialState(read_Lines)
                    if read_Lines[0] == 'F':
                        read_Lines = read_Lines.replace("F=", '').replace("\n",'')
                        add_FinalState(read_Lines)
                    if read_Lines[0] == 'D':
                        read_Lines = read_Lines.replace("D=",'').replace("\n",'')
                        add_Transitions(read_Lines)
            states_File = True
        else:
            messagebox.showwarning("Alerta", "El archivo no es un Txt")
    return states_File

#Definir los conjuntos
new_States = set()
new_Alphabet = set()
new_Initial = set()
new_Final = set()
new_Transitions = dict()

def add_States(lines):
    states = lines.split(",")
    for state in states:
        if state !="" or state !=" ":
            new_States.add(state)

def add_Alphabet(lines):
    alphabets = lines.split(",")
    for alphabet in alphabets:
        if alphabet !="" or alphabet !=" ":
            new_Alphabet.add(alphabet)

def add_InitialState(lines):
    initial_State = lines.split(",")
    for initial in initial_State:
        if initial !="" or initial !=" ":
            new_Initial.add(initial)

def add_FinalState(lines):
    final_State = lines.split(",")
    for final in final_State:
        if final !="" or final !=" ":
            new_Final.add(final)

def add_Transitions(lines):
    pass

#-------- Obtener y enviar datos ---
def send_States():
    return new_States

def send_Alphabet():
    return new_Alphabet

def send_InitialState():
    return new_Initial

def send_FinalState():
    return new_Final

def send_Transitions():
    return new_Transitions
    