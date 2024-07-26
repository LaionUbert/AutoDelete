#Header
'''
--- Autor: Laion Ubert Vieira Santos
--- Descrição: Script para deletar arquivos de pasta especifica a cada N dias
'''


#Importacao de modulos e libs
import os, datetime, shutil
import configparser
from datetime import datetime, timedelta


#Inicializacao do configparser
config = configparser.ConfigParser()
config.read("config.ini")


#Modificacao das configuracoes
##getters dos valores de input para as variaveis de mudanca
config_path = str(config.get('Default','config_path'))
config_time = int(config.get('Default','config_time'))

##alterar diretorio de controle para execucao das funcoes
setOSPath = os.chdir(os.path.join(os.getcwd(), config_path))

##alterar idade maxima dos arquivos
timeDelete = datetime.now() - timedelta(days = config_time)

##impressao dos valores atualizados das variaveis 
print(f"Diretório onde serão deletados os arquivos  :  {config_path}") #Imprime no terminal o caminho do diretorio
print(f"Serão deletados os arquivos anteriores a    :  {timeDelete}") #Imprime no terminal a data limite para deletar arquivos


#Funcoes
##funcao para listar arquivos a serem deletados
def listarArquivos(path = config_path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"Arquivo a ser deletado:   {entry.path}")
            elif entry.is_dir():
                listarArquivos(entry.path)

##funcao para deletar arquivos
def deletarArquivos():
    listarArquivos()
    shutil.rmtree(config_path, ignore_errors=True)
    print('Arquivos deletados com sucesso')

if datetime.now() > timeDelete:
    deletarArquivos()
