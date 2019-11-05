#!/usr/bin/python

import subprocess
import sys
import datetime

from datetime import datetime, timedelta


# importar fecha actual y le resta 5 dias

today = datetime.now()
date1 = today - timedelta(days=5)


# corre burp -al y se queda con la linea que tiene la ultima fecha

def burp():
	cmd = ["""burp -al | grep Backup | tail -1"""]
 	cmd1 = subprocess.check_output(cmd,shell=True)
	return cmd1

f1 = burp()

# convierte en una lista el strinmg que tiene la ultima fecha de respaldo

f2 = f1.split(' ')
# crea una veriable con la fecha y la convierte en formato fecha

f3 = f2[2]
f4 = datetime.strptime(f3, "%Y-%m-%d")


# compara las fechas y devuelve estado a nagios	

if f4 > date1:
	print ("OK - burp esta actualizado")
	sys.exit(0)
else:
	print ("CRITICAL - No hay respaldos de burp en los ultimos 5 dias")
	sys.exit(2)


