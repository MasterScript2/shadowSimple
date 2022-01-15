#!/usr/bin/env python
import os
import time
import colorama
import base64
import socket
import random
import re
import netifaces
from colorama import Fore
from socket import gethostbyaddr
from subprocess import Popen, PIPE

global port

class Col:
	red = Fore.RED
	blue = Fore.BLUE
	green = Fore.GREEN
	white = Fore.WHITE
	yellow = Fore.YELLOW
class Banners:
	banner_a = ("figlet shadow -f digital")
	banner_b = ("figlet shadow -f script")
	banner_c = ("figlet shadow -f shadow")
	banner_d = ("figlet shadow -f slant")
class Decore:
	decore = Col.yellow+"["+Col.red+"*"+Col.yellow+"]"

class Numbers:
	one = Col.red+"<"+Col.yellow+"1"+Col.red+">"
	two = Col.red+"<"+Col.yellow+"2"+Col.red+">"
	three = Col.red+"<"+Col.yellow+"3"+Col.red+">"
	four = Col.red+"<"+Col.yellow+"4"+Col.red+">"
	five = Col.red+"<"+Col.yellow+"5"+Col.red+">"
	Non = Col.red+"<"+Col.yellow+"0"+Col.red+">"
class listas:
	principal = [Numbers.one+" Escaner simple de puertos", Numbers.two+" Escanear puertos especificos", Numbers.three+" gethostbyname", Numbers.four+" myinfo", Numbers.Non+" Salir"]
banner_random = random.choice([Banners.banner_a, Banners.banner_b, Banners.banner_c, Banners.banner_d])
os.system(banner_random)
print(Col.yellow+"Esta herramiento necesita root para funcionar correctamente")
for lista in listas.principal:
	print(lista)
	time.sleep(0.2)
option = int(input(Col.red+"===> "+Col.blue))
if option == 1:
	ip_simple = input("Escriba la ip: ")
	print(Decore.decore+" Informacion recopilada")
	time.sleep(2)
	print(Decore.decore+" Comprobando informacion")
	time.sleep(2)
	print(Decore.decore+" Imprimiendo")
	time.sleep(2)
	print(Decore.decore+" Nombre del host", socket.gethostbyaddr(ip_simple)[0])
	time.sleep(1)
	print(Decore.decore+" Direccion addr:", ip_simple)
	time.sleep(1)
	print(Decore.decore+" Puertos Abiertos")
	os.system(f"python3 real -t {ip_simple}")
	print("\n"+Decore.decore+"Escaneo Finalizado"+Decore.decore)
elif option == 2:
    selection_max = int(input("Seleccione la cantidad de puertos, Max5: "))
    if selection_max == 1:
         only_ip = input("Escribe la ip: ")
         only_port = input("Escribe el puerto: ")
         os.system(f"python3 one_port -t {only_ip} -oP {only_port}")
         print(Decore.decore+" Finalizado")
    elif selection_max == 2:
    	d_ip = input("Escribe la ip: ")
    	d_a = input("Port#1: ")
    	d_b = input("Port#2: ")
    	os.system(f"python3 two_port -t {d_ip} -oP {d_a} -tP {d_b}")
    	print(Decore.decore+" Finalizado")
    elif selection_max == 3:
    	t_ip = input("Escribe la ip: ")
    	t_a = input("Port#1: ")
    	t_b = input("Port#2: ")
    	t_c = input("Port#3: ")
    	os.system(f"python3 three_port -t {t_ip} -oP {t_a} -tP {t_b} -ttP {t_c}")
    	print(Decore.decore+" Finalizado")
    elif selection_max == 4:
        f_ip = input("Escriba la ip: ")
        f_a = input("Port#1: ")
        f_b = input("Port#2: ")
        f_c = input("Port#3: ")
        f_d = input("Port#4: ")
        os.system(f"python3 four_port -t {f_ip} -oP {f_a} -tP {f_b} -ttP {f_c} -fP {f_d}")
        print(Decore.decore+" Finalizado")
    elif selection_max == 5:
    	c_ip = input("Escriba la ip: ")
    	c_a = input("Port#1: ")
    	c_b = input("Port#2: ")
    	c_c = input("Port#3: ")
    	c_d = input("Port#4_ ")
    	c_e = input("Port#5: ")
    	os.system(f"python3 max_port -t {c_ip} -oP {c_a} -tP {c_b} -ttP {c_c} -fP {c_d} -mX {c_e}")
    	print(Decore.decore+" Finalizado")
elif option == 3:
	host = input("Escriba la ip del host: "+Fore.RED)
	name = socket.gethostbyaddr(host)[0]
	print(Col.yellow+name)
elif option == 4:
	interfaces = netifaces.interfaces()[2]
	print(Col.red+"Interfas de red"+Col.yellow+"\n"+interfaces)
	time.sleep(1)
	print(Col.red+"Direccion IP Local----"+Col.yellow)
	time.sleep(1)
	os.system("hostname -I")
	time.sleep(1)
	print(Col.red+"Nombre de Maquina----"+Col.yellow)
	time.sleep(1)
	os.system("hostname")
	time.sleep(1)
	print(Col.red+"Nombre de Usuario----"+Col.yellow)
	time.sleep(1)
	os.system("whoami")
	time.sleep(1)
	print(Col.red+"Direccion IP publica"+Col.yellow)
	time.sleep(1)
	os.system("curl ifconfig.me")
	time.sleep(1)
elif option == 0:
	quit()