import os
import time
import socket
import argparse
from socket import gethostbyaddr
from time import sleep
from datetime import datetime

firt = argparse.ArgumentParser("")
firt.add_argument('-t', '--target', help="target")
firt.add_argument('-p', '--port', help="port")
firt = firt.parse_args()

global ip 
global port 

ip = str(firt.target)
port = int(firt.port)
def scan_port(ip, port):
	try:
		sock.connect( (ip, port) )
		return True
	except:
		return None

print("Starting shadow 1.0 ", "( https://github.com )", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("Shadow scan report for", socket.gethostbyaddr(firt.target)[0] , f"({firt.target})")
print("PORT      STATE   SERVICE")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
valor = scan_port(ip, port)
if valor == None:
	print(port, "/tcp   "+"down", None)
elif valor == True:
		if port == 1:
			print(port, "/tcp  "+"open "+"   tcpmux")
		elif port == 5:
			print(port, "/tcp  "+"open "+"   rje")
		elif port == 7:
			print(port, "/tcp  "+"open "+"   echo")
		elif port == 9:
			print(port, "/tcp  "+"open "+"   discard")
		elif port == 11:
			print(port, "/tcp  "+"open "+"   systat")
		elif port == 13:
			print(port, "/tcp  "+"open "+"   daytime")
		elif port == 17:
			print(port, "/tcp  "+"open "+"   qotd")
		elif port == 18:
			print(port, "/tcp  "+"open "+"   msp")
		elif port == 19:
			print(port, "/tcp  "+"open "+"   chargen")
		elif port == 20:
			print(port, "/tcp  "+"open "+"   ftpS-data")
		elif port == 21:
			print(port, "/tcp  "+"open "+"   ftp-control")
		elif port == 22:
			print(port, "/tcp  "+"open "+"   ssh")
		elif port == 23:
			print(port, "/tcp  "+"open "+"   telnet")
		elif port == 25:
			print(port, "/tcp  "+"open "+"   smtp")
		elif port == 37:
			print(port, "/tcp  "+"open "+"   time")
		elif port == 39:
			print(port, "/tcp  "+"open "+"   rlp")
		elif port == 42:
			print(port, "/tcp  "+"open"+"    nameserver")
		elif port == 43:
			print(port, "/tcp  "+"open "+"   nickname")
		elif port == 49:
			print(port, "/tcp  "+"open "+"   tacacs")
		elif port == 50:
			print(port, "/tcp  "+"open "+"   re-mail-ck")
		elif port == 53:
			print(port, "/tcp  "+"open "+"   domain")
		elif port == 63:
			print(port, "/tcp  "+"open "+"   whois++")
		elif port == 66:
			print(port, "/tcp  "+"open "+"   OracleSQLNet")
		elif port == 70:
			print(port, "/tcp  "+"open "+"   gopher")
		elif port == 79:
			print(port, "/tcp  "+"open "+"   finger")
		elif port == 80:
			print(port, "/tcp  "+"open "+"   http")
		elif port == 88:
			print(port, "/tcp  "+"open "+"   kerberos")
		elif port == 95:
			print(port, "/tcp  "+"open "+"   supdup")
		elif port == 101:
			print(port, "/tcp  "+"open "+"   hostname")
		elif port == 107:
			print(port, "/tcp  "+"open "+"   rtelnet")
		elif port == 109:
			print(port, "/tcp  "+"open "+"   pop2")
		elif port == 110:
			print(port, "/tcp  "+"open "+"   pop3")
		elif port == 111:
			print(port, "/tcp  "+"open "+"   sunrpc")
		elif port == 113:
			print(port, "/tcp  "+"open "+"   auth")
		elif port == 115:
			print(port, "/tcp  "+"open "+"   sftp")
		elif port == 117:
			print(port, "/tcp  "+"open "+"   uupc-path")
		elif port == 119:
			print(port, "/tcp  "+"open "+"   nntp")
		elif port == 123:
			print(port, "/tcp  "+"open "+"   ntp")
		elif port == 135:
			print(port, "/tcp  "+"open "+"   epmap")
		elif port == 139:
			print(port, "/tcp  "+"open "+"   netbios-ssn")
		elif port == 143:
			print(port, "/tcp  "+"open "+"   imap")
		elif port == 174:
			print(port, "/tcp  "+"open "+"   mailq")
		elif port == 177:
			print(port, "/tcp  "+"open "+"   xdmcp")
		elif port == 178:
			print(port, "/tcp  "+"open "+"   nextstep")
		elif port == 179:
			print(port, "/tcp  "+"open "+"   bgp")
		elif port == 194:
			print(port, "/tcp  "+"open "+"   irc")
		elif port == 199:
			print(port, "/tcp  "+"open "+"   smux")
		elif port == 201:
			print(port, "/tcp  "+"open "+"   at-rtmp")
		elif port == 202:
			print(port, "/tcp  "+"open "+"   at-nbp")
		elif port == 204:
			print(port, "/tcp  "+"open "+"   at-echo")
		elif port == 206:
			print(port, "/tcp  "+"open "+"   at-zis")
		elif port == 209:
			print(port, "/tcp  "+"open "+"   qmtp")
		elif port == 210:
			print(port, "/tcp  "+"open "+"   z39.50")
		elif port == 213:
			print(port, "/tcp  "+"open "+"   ipx")
		elif port == 220:
			print(port, "/tcp  "+"open "+"   imap3")
		elif port == 245:
			print(port, "/tcp  "+"open "+"   link")
		elif port == 347:
			print(port, "/tcp  "+"open "+"   fatserv")
		elif port == 363:
			print(port, "/tcp  "+"open "+"   rsvp_tunnel")
		elif port == 369:
			print(port, "/tcp  "+"open "+"   rpc2portmap")
		elif port == 370:
			print(port, "/tcp  "+"open "+"   codaauth2")
		elif port == 372:
			print(port, "/tcp  "+"open "+"   ulistproc")
		elif port == 389:
			print(port, "/tcp  "+"open "+"   Idap")
		elif port == 427:
			print(port, "/tcp  "+"open "+"   svrloc")
		elif port == 434:
			print(port, "/tcp  "+"open "+"   mobileip-agent")
		elif port == 435:
			print(port, "/tcp  "+"open "+"   mobilip-mn")
		elif port == 443:
			print(port, "/tcp "+"open "+"   https")
		elif port == 444:
			print(port, "/tcp  "+"open "+"   snpp")
		elif port == 445:
			print(port, "/tcp  "+"open "+"   microsoft-ds")
		elif port == 465:
			print(port, "/tcp  "+"open "+"   smtps")
		elif port == 587:
			print(port, "/tcp  "+"open "+"   smtp")
		elif port == 993:
			print(port, "/tcp  "+"open "+"   imaps")	
		else:
			print(port, "/tcp  "+"open "+"   -----")
else:
	pass
	
numero = time.time()
decimales = round(numero, 3)
print("\nshadow done: 1 IP address (1 host up) scanned in", decimales, "seconds")