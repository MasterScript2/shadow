import os
import time
import socket
import argparse
from socket import gethostbyaddr

parse = argparse.ArgumentParser("tcp options")
parse.add_argument('-t', '--target', help="DireccionIP")
parse = parse.parse_args()
'''
host = socket.gethostbyaddr(parse.target)[0]
print(host, "(", parse.target, ")")
'''
def funtions():
	try:
		ini = socket.gethostbyaddr(parse.target)[0]
		return True
	except:
		return None
sintax = funtions()
if sintax == None:
	pass 
elif sintax == True:
	eggs = socket.gethostbyaddr(parse.target)[0]
	print(eggs, "("+parse.target+")")
else:
	pass