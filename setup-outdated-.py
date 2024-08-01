#Header
'''
--- Autor: Laion Ubert Vieira Santos
--- Descrição: Interface grafica para configuração dos parametros do fileScript.py com a biblioteca TKinter.
'''


#Importacao dos modulos
import configparser, os
import fileScript
from tkinter import *
from tkinter import ttk


#Head
root = Tk()
root.title("AutoDelete")
root.geometry('475x375')
root.resizable(0,0)
root.tk.call('tk','scaling',1)
#***root.iconbitmap('media/Logo.ico')

#Inicializacao do configparser
config = configparser.ConfigParser()
config.read("config.ini")


#Funcoes
##pegar valores do input
def getValue():
    pathInput = str(configPathEntry.get())
    timeInput = str(configTimeEntry.get())

    #validar input da variavel 'pathInput' (se/senao existir)
    if os.path.exists(pathInput) == True: #Se verdadeiro, irá definir o input na variavel 'pathInput'
        config.set('Default', 'config_path', pathInput)
        print(config.get('Default','config_path'))
    else: #Se falso, irá retornar mensagem de erro
        print("Diretório de destino não acessível. Favor verificar se o caminho existe e está disponível para Leitura/Escrita")
 
    #validar input da variavel 'timeInput' (se/senao for numerico)
    if (timeInput.isnumeric()) and (int(timeInput) >= 0): #Se verdadeiro, irá definir o input na variavel 'timeInput'
        config.set('Default', 'config_time', timeInput)
        print(config.get('Default','config_time'))
    else: #Se falso, irá retornar mensagem de erro
        print("Tipo de dado incorreto. Favor usar apenas números inteiros positivos") 
        
    #gravar valores das variaveis no arquivo 'config.ini'
    with open ('config.ini', 'w') as configfile:
        config.write(configfile)  

##limpar valor da variavel 'config_path'
def clearPathValue(): #Limpar valor do campo 'config_path'
    config.set('Default', 'config_path','Null')
    configPathEntry.delete(0, END)
    with open ('config.ini', 'w') as configfile:
        config.write(configfile)  

##limpar valor da variavel 'config_time'
def clearTimeValue():  #Limpar valor do campo 'config_time'
    config.set('Default', 'config_time','0')
    configTimeEntry.delete(0, END)
    with open ('config.ini', 'w') as configfile:
        config.write(configfile)  

def runManualDelete():
    print('Deletando Manualmente')
    fileScript.deletarArquivos()
    
    
def runManualCopy():
    print('Copiando Manualmente')
    fileScript.copiarArquivos()

#Elementos da janela
frame = Frame(root)

##labels
h1Label = Label(
    frame, text="Setup ", font=('Arial', 18,'bold'))
configPathLabel = Label(
    frame, text="Informe o diretório a ser deletado: ", font=('Arial', 12))
configTimeLabel = Label(
    frame, text="Informe a idade máxima dos arquivos (em dias): ",font=('Arial', 12), justify='left')

##buttons
clearPathButton = Button(frame, text="Limpar", font=('Arial', 12), command=clearPathValue)
clearTimeButton = Button(frame, text="Limpar", font=('Arial', 12), command=clearTimeValue)
saveInputButton = Button(frame, text="Salvar", font=('Arial', 18), command=getValue)
runDeleteInputButton = Button(frame, text="Deletar Manualmente", font=('Arial', 18), command=runManualDelete)
runCopyInputButton = Button(frame, text="Copiar Manualmente", font=('Arial', 18), command=runManualCopy)


##entries
configPathEntry = Entry(frame, width=60, font=('Arial', 12))
configTimeEntry = Entry(frame, width=10, font=('Arial', 12))

##formatacao do grid
h1Label.grid(column=0, row=0, columnspan=4, pady=20)

###formatacao dos campos de edicao de caminho
configPathLabel.grid(sticky=W, row=1, column=0, columnspan=4)
clearPathButton.grid(row=1, column=3, pady=5, padx=10)
configPathEntry.grid(sticky=W, row=2, column=0, columnspan=4)

###formatacao dos campos de edicao de tempo
configTimeLabel.grid(sticky=W, row=3, column=0, columnspan=4)
clearTimeButton.grid(row=3, column=3, pady=10, padx=10, columnspan=4)
configTimeEntry.grid(sticky=W, row=4, column=0, columnspan=4)

###formatacao do botao de salvar
saveInputButton.grid(row=5, column=0, pady=10, padx=5, columnspan=4)
runDeleteInputButton.grid(row=6, column=0, pady=10, padx=5,columnspan=4)
runCopyInputButton.grid(row=7, column=0, pady=10, padx=5,columnspan=4)


frame.pack()


#Loop da janela
root.mainloop()
