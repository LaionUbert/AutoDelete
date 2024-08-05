#Header
# --- Autor: Laion Ubert Vieira Santos
# --- Descrição: Interface grafica para configuração dos parametros do fileScript.py com a biblioteca TKinter e Tkinter Designer
# --- e a execução manual da exlusao e copia dos arquivos.


import configparser, os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path


# Inicializacao do configparser
config = configparser.ConfigParser()
configFile = r'config.ini'
config.read(configFile)
print(config.get("Default", "config_path"))


# Funcoes de execucao
## pegar valores do input
def saveValue():
    copyInput = str(configCopyEntry.get())
    pathInput = str(configPathEntry.get())
    timeInput = str(configTimeEntry.get())

    # validar input da variavel 'copyInput' (se/senao existir)
    if os.path.exists(copyInput) == True: #Se verdadeiro, irá definir o input na variavel 'pathInput'
        config.set('Default', 'config_path_copy', copyInput)
        print(config.get('Default','config_path'))
    elif copyInput == "Null": # Se falso, irá retornar mensagem de erro
        print("Nenhum diretório selecionado")
    else: 
        print("Diretório de destino não acessível. Favor verificar se o caminho existe e está disponível para Leitura/Escrita")

    # validar input da variavel 'pathInput' (se/senao existir)
    if os.path.exists(pathInput) == True: #Se verdadeiro, irá definir o input na variavel 'pathInput'
        config.set('Default', 'config_path', pathInput)
        print(config.get('Default','config_path'))
    elif copyInput == "Null": # Se falso, irá retornar mensagem de erro
        print("Nenhum diretório selecionado")
    else: 
        print("Diretório de destino não acessível. Favor verificar se o caminho existe e está disponível para Leitura/Escrita")
        
    # validar input da variavel 'timeInput' (se/senao for numerico)
    if (timeInput.isnumeric()) and (int(timeInput) > 0): # Se verdadeiro, irá definir o input na variavel 'timeInput'
        config.set('Default', 'config_time', timeInput)
        print(config.get('Default','config_time'))
    elif timeInput == 0: # Se for 0, irá retornar mensagem de erro
        print("Idade não pode ser igual ou menor que 0")
    else: # Se falso, irá retornar mensagem de erro
        print("Tipo de dado incorreto. Favor usar apenas números inteiros positivos") 
        
    # gravar valores das variaveis no arquivo configFile
    with open (configFile, 'w') as configfile:
        config.write(configfile)  


## limpar valor da variavel 'config_path_copy'
def clearCopyValue():
    configCopyEntry.delete(0)
    config.set('Default', 'config_path_copy', 'Null')
    with open (configFile, 'w') as configfile:
        config.write(configfile)  

## limpar valor da variavel 'config_path'
def clearPathValue(): # Limpar valor do campo 'config_path'
    config.set('Default', 'config_path','Null')
    configPathEntry.delete(0)
    with open (configFile, 'w') as configfile:
        config.write(configfile)  

## limpar valor da variavel 'config_time'
def clearTimeValue():  # Limpar valor do campo 'config_time'
    config.set('Default', 'config_time','0')
    configTimeEntry.delete(0)
    with open (configFile, 'w') as configfile:
        config.write(configfile)  

# Alterar opcoes de execucao
## habilitar/desabilitar copia
def habilitarCopia():
    config.set('Tweaks', 'option_copiar_arquivos', '1')
    with open (configFile, 'w') as configfile:
        config.write(configfile) 

def desabilitarCopia():
    config.set('Tweaks', 'option_copiar_arquivos', '0')
    with open (configFile, 'w') as configfile:
        config.write(configfile) 

## habilitar/desabilitar exclusao
def habilitarDeletar():
    config.set('Tweaks', 'option_deletar_arquivos', '1')
    with open (configFile, 'w') as configfile:
        config.write(configfile) 

def desabilitarDeletar():
    config.set('Tweaks', 'option_deletar_arquivos', '0')
    with open (configFile, 'w') as configfile:
        config.write(configfile) 

# Acessar diretorios
## acessar diretorio de copia
def openCopy():    
    return 0

## acessar diretorio gerenciado
def openPath():
    return 0


# Execucao Manual
## executar exclusao manual
def runManualDelete():
    import fileScript
    print('Deletando Manualmente')
    fileScript.deletarArquivos()
    
## executar copia manual
def runManualCopy():
    import fileScript
    print('Copiando Manualmente')
    fileScript.copiarArquivos()


# Formatacao e Estilizacao da GUI
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"app\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

## configuracao do canvas
window = Tk()

window.geometry("450x400")
window.configure(bg = "#FFFFFF")
window.title("AutoFile Setup")
window.iconbitmap(r'app\assets\frame0\Logo.ico')


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    5.684341886080802e-14,
    450.0,
    400.00000000000006,
    fill="#D9D9D9",
    outline="")

## botao de limpar diretorio de copia
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
clearCopyButton = Button(
    image=button_image_1,
    text='Limpar',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= clearCopyValue,
    relief="flat"
)
clearCopyButton.place(
    x=346.0,
    y=111.0,
    width=75.0,
    height=25.0
)

## botao para habilitar copia dos arquivos
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
habilitarCopiaButton = Button(
    image=button_image_2,
    text='Habilitar',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= habilitarCopia,
    relief="flat"
)
habilitarCopiaButton.place(
    x=261.0,
    y=238.0,
    width=75.0,
    height=25.0
)

## botao para habilitar exclusao dos arquivos
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
habilitarDeletarButton = Button(
    image=button_image_3,
    text='Habilitar',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= habilitarDeletar,
    relief="flat"
)
habilitarDeletarButton.place(
    x=261.0,
    y=273.0,
    width=75.0,
    height=25.0
)

## botao para desabilitar exclusao dos arquivos
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
desabilitarDeletarButton = Button(
    image=button_image_4,
    text='Desabilitar',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= desabilitarDeletar,
    relief="flat"
)
desabilitarDeletarButton.place(
    x=346.0,
    y=273.0,
    width=75.0,
    height=25.0
)

## botao para desabilitar copia dos arquivos
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
desabilitarCopiaButton = Button(
    image=button_image_5,
    text='Desabilitar',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= desabilitarCopia,
    relief="flat"
)
desabilitarCopiaButton.place(
    x=346.0,
    y=238.0,
    width=75.0,
    height=25.0
)

## botao de limpar
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
clearTimeButton = Button(
    image=button_image_6,
    text='Limpar',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= clearTimeValue,
    relief="flat"
)
clearTimeButton.place(
    x=346.0,
    y=202.0,
    width=75.0,
    height=25.0
)

## botao de limpar campo de diretorio gerenciado
button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
clearPathButton = Button(
    image=button_image_7,
    text='Limpar',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= clearPathValue,
    relief="flat"
)
clearPathButton.place(
    x=346.0,
    y=167.0,
    width=75.0,
    height=25.0
)

## botao de salvar os dados de configuracao
button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
saveValueButton = Button(
    image=button_image_8,
    text='Salvar',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= saveValue,
    relief="flat"
)
saveValueButton.place(
    x=28.0,
    y=343.0,
    width=75.0,
    height=25.0
)

## botao de executar a copia manualmente
button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
runManualCopyButton = Button(
    image=button_image_9,
    text='Copiar Manualmente',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= runManualCopy,
    relief="flat"
)
runManualCopyButton.place(
    x=112.0,
    y=343.0,
    width=150.0,
    height=25.0
)

## botao de executar a exclusao manualmente
button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
runManualDeleteButton = Button(
    image=button_image_10,
    text='Deletar Manualmente',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= runManualDelete,
    relief="flat"
)
runManualDeleteButton.place(
    x=271.0,
    y=343.0,
    width=150.0,
    height=25.0
)

## botao de abrir o diretorio de copia
button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
openCopyButton = Button(
    image=button_image_11,
    text='Acessar Diretório de Cópia',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= openCopy,
    relief="flat"
)
openCopyButton.place(
    x=28.0,
    y=308.0,
    width=193.0,
    height=25.0
)

## botao de abrir o diretorio gerenciado
button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
openPathButton = Button(
    image=button_image_12,
    text='Acessar Diretório Gerenciado',
    font=("Arial", 10),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command= openPath,
    relief="flat"
)
openPathButton.place(
    x=231.0,
    y=308.0,
    width=190.0,
    height=25.0
)

## campo de entrada do diretorio de copia
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    182.0,
    123.5,
    image=entry_image_3
)
configCopyEntry = Entry(
    bd=0,
    bg="#B3B3B3",
    fg="#000716",
    highlightthickness=0
)
configCopyEntry.place(
    x=33.0,
    y=111.0,
    width=298.0,
    height=23.0
)

## campo de entrada do diretorio gerenciado
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    182.0,
    179.5,
    image=entry_image_1
)
configPathEntry = Entry(
    bd=0,
    bg="#B3B3B3",
    fg="#000716",
    highlightthickness=0
)
configPathEntry.place(
    x=33.0,
    y=167.0,
    width=298.0,
    height=23.0
)

## campo de entrada da idade do arquivo
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    291.0,
    214.5,
    image=entry_image_2
)
configTimeEntry = Entry(
    bd=0,
    bg="#B3B3B3",
    fg="#000716",
    highlightthickness=0
)
configTimeEntry.place(
    x=251.0,
    y=202.0,
    width=80.0,
    height=23.0
)

## criacao dos textos
canvas.create_text(
    142.0,
    32.0,
    anchor="nw",
    text="AutoFile Setup",
    fill="black",
    font=("Arial", 24 * -1, "bold")
)

canvas.create_text(
    28.0,
    92.0,
    anchor="nw",
    text="Caminho do diretório a ser copiado:",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    28.0,
    148.0,
    anchor="nw",
    text="Caminho do diretório a ser gerenciado:",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    28.0,
    208.0,
    anchor="nw",
    text="Idade máxima dos arquivos (em dias):",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    28.0,
    243.0,
    anchor="nw",
    text="Habilitar/Desabilitar cópia dos dados:",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    28.0,
    279.0,
    anchor="nw",
    text="Habilitar/Desabilitar deleção dos dados:",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    48.0,
    348.0,
    anchor="nw",
    text="Salvar",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    128.0,
    348.0,
    anchor="nw",
    text="Copiar Manualmente",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    285.0,
    348.0,
    anchor="nw",
    text="Deletar Manualmente",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    49.0,
    313.0,
    anchor="nw",
    text="Acessar Diretório de Cópia",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    242.0,
    313.0,
    anchor="nw",
    text="Acessar Diretório Gerenciado",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    353.0,
    243.0,
    anchor="nw",
    text="Desabilitar",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    353.0,
    278.0,
    anchor="nw",
    text="Desabilitar",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    275.0,
    243.0,
    anchor="nw",
    text="Habilitar",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    275.0,
    278.0,
    anchor="nw",
    text="Habilitar",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    364.0,
    207.0,
    anchor="nw",
    text="Limpar",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    364.0,
    172.0,
    anchor="nw",
    text="Limpar",
    fill="black",
    font=("Arial", 12 * -1)
)

canvas.create_text(
    364.0,
    116.0,
    anchor="nw",
    text="Limpar",
    fill="black",
    font=("Arial", 12 * -1)
)


window.resizable(False, False)
window.mainloop()
