#Header (WIP)
'''
--- Interface grafica para configuração dos parametros do deleteScript.py com a biblioteca TKinter.

'''


#Importacao dos modulos
import configparser, os
from tkinter import *
from tkinter import ttk


#Head
window = Tk()
window.title("hello world")
window.geometry('500x500')
window.tk.call('tk','scaling',1)

#Inicializacao do configparser
config = configparser.ConfigParser()
config.read("config.ini")


#Funcoes
##pegar valores do input
def getValue():
    pathInput = str(configPathEntry.get())
    timeInput = str(configTimeEntry.get())

    #validar input da variavel 'timeInput' (se/senao for numerico)
    timeInputCheck = timeInput.isnumeric()
    pathInputCheck = os.path.exists(pathInput)
    if timeInputCheck == True: #Se verdadeiro, irá definir o input na variavel 'timeInput'
        config.set('Default', 'config_time', timeInput)
        print(config.get('Default','config_time'))
    else: #Se falso, irá retornar mensagem de erro
        print("tipo de dado incorreto, favor usar apenas números positivos") 

    #validar input da variavel 'pathInput' (se/senao existir)
    if pathInputCheck == True: #Se verdadeiro, irá definir o input na variavel 'pathInput'
        config.set('Default', 'config_path', pathInput)
        print(config.get('Default','config_path'))
    else: #Se falso, irá retornar mensagem de erro
        print("caminho nao existe, favor verificar se a pasta está dispponível e com permissão de Leitura/Escrita pelo usuário")
        
    #gravar valores das variaveis no arquivo 'config.ini'
    with open ('config.ini', 'w') as configfile:
        config.write(configfile)  


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


#Loop da janela
window.mainloop()
