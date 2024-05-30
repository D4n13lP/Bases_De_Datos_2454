"""
Programa que funciona para sustituir los caracteres en hexadecimal a su versión en utf-8 
específicamente el caracter é
Actualmente no se ejecuta puesto que los archivos ya han sido modificados
"""
import os
for j in range(3,10):
    # Lee el archivo original
    archivo = "meteorología_201"+ str(j) +".json"
    # Se lee y cambia el acento en hexadecimal
    with open(archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    for i, linea in enumerate(lineas):
        lineas[i] = linea.replace("\\"+"\\u00e9", 'é')

    # Se guarda el nuevo archivo
    with open(archivo, 'w', encoding='utf-8') as f:
        f.writelines(lineas)

for j in range(0,4):
    # Lee el archivo original
    archivo = "meteorología_202"+ str(j) +".json"
    # Se lee y cambia el acento en hexadecimal
    with open(archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    for i, linea in enumerate(lineas):
        lineas[i] = linea.replace("\\"+"\\u00e9", 'é')

    # Se guarda el nuevo archivo
    with open(archivo, 'w', encoding='utf-8') as f:
        f.writelines(lineas)