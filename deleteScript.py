#Script para deletar arquivos de pasta especifica a cada N dias

import os, datetime, shutil
from datetime import datetime, timedelta

config_path = r"C:\Users\laion.santos\Desktop\testealvo"
config_time = 1

#contentPath = config_path.read()
setOSPath = os.chdir(os.path.join(os.getcwd(), config_path))

#contentTime = int(config_time.read())
timeNow = datetime.now()
timeDelete = timeNow - timedelta(days = config_time)

print(f"Diretório onde serão deletados os arquivos  :  {config_path}")
print(f"Serão deletados os arquivos anteriores a    :  {timeDelete}")

def listarArquivos(path = config_path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"Arquivo a ser deletado:   {entry.path}")
            elif entry.is_dir():
                listarArquivos(entry.path)

def deletarArquivos():
    listarArquivos()
    shutil.rmtree(config_path, ignore_errors=True)
    print('Arquivos deletados com sucesso')

if timeNow > timeDelete:
    deletarArquivos()
