#Header
'''
--- Autor: Laion Ubert Vieira Santos
--- Descrição: Script para copiar e deletar arquivos de pasta especifica a cada N dias
'''


# Importacao de modulos e libs
import os, datetime, shutil, pathlib
import configparser
from datetime import datetime, timedelta


# Inicializacao do configparser
config = configparser.ConfigParser()
configFile = r'config.ini'
config.read(configFile)


# Modificacao das configuracoes
## getters dos valores de input para as variaveis de mudanca
config_path = str(config.get('Default','config_path'))
config_path_copy = str(config.get('Default','config_path_copy'))
config_time = int(config.get('Default','config_time'))
selfDir = os.path.dirname(__file__)

## alterar idade maxima dos arquivos
timeDelete = datetime.now() - timedelta(days = config_time)

## impressao dos valores atualizados das variaveis 
print(f"Diretório onde serão deletados os arquivos  :  {config_path}") # Imprime no terminal o caminho do diretorio
print(f"Serão deletados os arquivos anteriores a    :  {timeDelete}") # Imprime no terminal a data limite para deletar arquivos


# Funcoes
## funcao para listar arquivos a serem deletados
def listarArquivos(path = os.chdir(os.path.join(os.getcwd(), config_path_copy))):
    with os.scandir(path) as entries:
        try:
            for entry in entries:
                if entry.is_file():
                    print(f"Arquivo selecionado:   {entry.path}")
                elif entry.is_dir():
                    listarArquivos(entry.path)
        except PermissionError:
            print(f'Arquivo com acesso negado: {path}')

## funcao para deletar arquivos
def deletarArquivos():
    if os.path.exists(config_path) == True:
        os.chdir(os.path.join(os.getcwd(), config_path))
        print('Listando arquivos para deletar:')
        listarArquivos()
        shutil.rmtree(config_path, ignore_errors=True)
        print('Arquivos deletados com sucesso')
        os.chdir(os.path.join(os.getcwd(), selfDir))
    else:
        print("Diretório de destino não acessível. Favor verificar se o caminho existe e está disponível para Leitura/Escrita")

## funcao para copiar arquivos
def copiarArquivos():
    if os.path.exists(config_path) and os.path.exists(config_path_copy) == True:
        os.chdir(os.path.join(os.getcwd(), config_path))
        listarArquivos(config_path_copy)
        shutil.copytree(config_path_copy, config_path, dirs_exist_ok=True)
        print('Arquivos copiados com sucesso')
        os.chdir(os.path.join(os.getcwd(), selfDir))
    elif os.path.exists(config_path) == False and os.path.exists(config_path_copy) == True:
        print("Diretório de destino não acessível. Favor verificar se o caminho existe e está disponível para Leitura/Escrita")
    elif os.path.exists(config_path_copy) == False:
        print("Diretório de origem não acessível. Favor verificar se o caminho existe e está disponível para Leitura/Escrita")


# listarArquivos()
# Execucao das funcoes com base na diferenca de tempo
if datetime.now() > timeDelete:
    if config.getboolean('Tweaks','option_deletar_arquivos') == 1:
        deletarArquivos()
if config.getboolean('Tweaks','option_copiar_arquivos') == 1:
    copiarArquivos()
