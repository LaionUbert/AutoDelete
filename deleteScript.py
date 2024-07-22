"""Script para deletar arquivos de pasta especifica a cada N dias"""
import os, time
from pathlib import Path

MAIN_DIR = Path(__file__).parent #Define diretório local do aplicativo
TIME_FILE = MAIN_DIR / 'config/time.txt' #Aponta o arquivo com a informação
PATH_FILE = MAIN_DIR / 'config/path.txt' #Aponta o arquivo com o diretório a ser manipulado


configPath = open(PATH_FILE)
configTime = open(TIME_FILE)

contentPath = configPath.read()
path = os.chdir(os.path.join(os.getcwd(), contentPath))

contentTime = int(configTime.read())
timeNow = time.time()
timeDelete = timeNow - (contentTime*86400)

print(f"O Diretório é: {contentPath}")
print(f"O Tempo de Deleção é: {timeNow}")
print(f"O Novo tempo é: {timeDelete}")

listaDeArquivos = os.listdir(path)

for i in listaDeArquivos:
    localArquivo = os.path.join(os.getcwd(), i)
    tempoArquivo = os.stat(localArquivo).st_mtime
    
    if (timeNow > timeDelete):
        print(f'Deleting: {i}')
        #os.remove(configPath.read())


configPath.close
configTime.close
