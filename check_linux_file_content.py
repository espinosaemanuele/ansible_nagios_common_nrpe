#!/usr/bin/python

import sys
import os
import glob

# argumento de ubicacion del archivo
path_file = sys.argv[1]
# argumento de text a comparar
text = sys.argv[2]

# chequear si el directorio existe si no termina el script

if (os.path.isdir(path_file) != True) :
	print ("No se encontro la carpeta")
	sys.exit(2)

#funcion que busca el archivo mas reciente de extencion .csv
def file_csv(filepath2):
	list_of_files = glob.glob(path_file+"*.csv")
	latest_file = max(list_of_files, key=os.path.getctime)
	return latest_file

file_to_read = file_csv(path_file)

# funcion que lee la primera linea del archivo de texto
def readtext(filepath):
	op = open(filepath, "r")
	rd = op.readline()
	stp = rd.rstrip('\n')
	data = stp.replace(';','').replace(' ','')
	return data
	op.close()

firstline = readtext(file_to_read)

#funcion if para comparar que coincidan las lineas de texto
if text == firstline:
	print ("OK - sensors order is right")
	sys.exit(0)
elif text != firstline:
	print ("CRITICAL - sensors order is wrong")
	print firstline
	print text
	sys.exit(2)
else:
	print ("UNKNOWN ERROR")
	sys.exit(3)
