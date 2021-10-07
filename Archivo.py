from tkinter import filedialog

#Agregar el archivo de texto
def add_File():
    new_File = filedialog.askopenfilename(title="Add File", initialdir="c:/desktop", filetypes=(("txt files","*.txt"),("todos los archivos","*.*")))
    if new_File != '':
        with open(new_File) as n_files:
            lines_saved = n_files.readlines()
        n_files.close()

        data_Saved = []
        for lines_read in lines_saved:
            lines_read = lines_read.replace("\n","")
            lines_read = lines_read.replace("{","")
            lines_read = lines_read.replace("}","")
            lines_read = lines_read.replace("=","")
            lines_read = lines_read.replace(" ","")
            lines_read = lines_read.replace(",","")
            data_Saved.append(lines_read)

    return data_Saved

def compare_Automaton():
    pass

