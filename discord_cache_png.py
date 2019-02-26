#!/usr/bin/env python3

import os

cont = 0

if "Cache" in os.getcwd(): #Verifica se esta no dir correto
    os.getcwd()    # Pega o dir atual
    for fileName in os.listdir("."):
        if "data" in fileName or "index" in fileName or "discord_cache_png.py" in fileName:
            continue     #Filtra arquivos que não sejam fotos, caso não seja, ele pula para o proximo loop
        else:
            print("Arquivo renomeado: {}".format(fileName))
            os.rename(fileName, fileName + ".png")   #Renomeia para a extensão PNG
            cont += 1
    print("Foram renomeados {} arquivos.".format(cont))
else:
    print("Estou no diretorio incorreto!")
