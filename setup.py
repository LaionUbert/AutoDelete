#Header (WIP)
'''
--- Interface grafica para configuração dos parametros do deleteScript.py com a biblioteca TKinter.

'''


#Importacao dos modulos
import configparser
from tkinter import *
from tkinter import ttk


#Head
window = Tk()
window.title("hello world")
window.geometry('500x500')
window.tk.call('tk','scaling',1)

#inicializacao do configparser
config = configparser.ConfigParser()
config.read("config.ini")


#funcoes
##validar dados (WIP)
'''def isInt(n):
    try:
        float(n)
    except:
        return False
    else:
        return float(n).is_integer()'''

'''def isStr():'''
    

##pegar valores do input
def getValue():
    pathInput = str(configPathEntry.get())
    timeInput = str(configTimeEntry.get())

    config.set('Default', 'config_time', timeInput)
    config.set('Default','config_path', pathInput)
    
    with open ('config.ini', 'w') as configfile:
        config.write(configfile) 
    
    print(timeInput)
    print(pathInput)
    

    #validar input (WIP)
    '''if inputConfigPath == isInt(True):
        print('true')
    else:
        print("false")'''

#Elementos da janela
##labels
h1Label = Label(window, text="Setup AutoDelete", font=('Arial', 20))
configPathLabel = Label(
    window, text="Informe o diretório a ser deletado: ", font=('Arial', 16))
configTimeLabel = Label(
    window, text="Informe a idade máxima dos arquivos (em dias): ",font=('Arial', 16))


##buttons
saveInputButton = Button(window, text="Salvar", font=('Arial', 20), command=getValue)


##entries
configPathEntry = Entry(window)
configTimeEntry = Entry(window)


##formatacao do grid
h1Label.grid(column=0, row=0, columnspan=2)

configPathLabel.grid(row=1, column=0)
configPathEntry.grid(row=1, column=1)

configTimeLabel.grid(row=2, column=0)
configTimeEntry.grid(row=2, column=1)

saveInputButton.grid(row=3, column=0, columnspan=2)


#loop da janela
window.mainloop()
