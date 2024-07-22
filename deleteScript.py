"""Script para deletar arquivos de pasta especifica a cada N dias"""
import os, time
from pathlib import Path

MAIN_DIR = Path(__file__).parent #Define diretório local do aplicativo
TIME_FILE = MAIN_DIR / 'config/time.txt' #Aponta o arquivo com a informação
PATH_FILE = MAIN_DIR / 'config/path.txt' #Aponta o arquivo com o diretório a ser manipulado

timeNow = time.time()

configPath = open(PATH_FILE)
configTime = open(TIME_FILE)
contentPath = configPath.read()
contentTime = int(configTime.read())

print(f"O Diretório é: {contentPath}")
print(f"O Tempo de Deleção é: {timeNow}")
print(f"O Novo tempo é: {((timeNow) - contentTime)}")

configPath.close
configPath.close
