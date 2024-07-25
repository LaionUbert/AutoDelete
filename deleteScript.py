#Header (WIP)
'''
--- Script para deletar arquivos de pasta especifica a cada N dias

'''

#Importacao de modulos e libs
import os, datetime, shutil
import configparser
from datetime import datetime, timedelta


#inicializacao do configparser
config = configparser.ConfigParser()
config.read("config.ini")


config_path = str(config.get('Default','config_path'))
config_time = int(config.get('Default','config_time'))

setOSPath = os.chdir(os.path.join(os.getcwd(), config_path))

timeNow = datetime.now()
timeDelete = timeNow - timedelta(days = config_time)

print(f"Diretório onde serão deletados os arquivos  :  {config_path}")
print(f"Serão deletados os arquivos anteriores a    :  {timeDelete}")


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

if timeNow > timeDelete:
    deletarArquivos()
