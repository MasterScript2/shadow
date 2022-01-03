#!/usr/bin/env python
import os
import argparse
import time

setup = argparse.ArgumentParser("options")
setup.add_argument('-t', '--target', help="IP")
setup.add_argument('-sN', '--scan_tcp', help="Escaneos de puertos tcp")
setup.add_argument('-sP', '--scanHost', help="ver hosts de la red")
setup.add_argument('-rG', '--range', help="range")
setup.add_argument('-iN', '--inet', help="inet")
setup.add_argument('-fP', '--firtPort', help="PuertoUnico")
setup.add_argument('-p', '--port', help="port")
setup = setup.parse_args()

if setup.scan_tcp == "go":
	os.system(f"python3 tcp.py -t {setup.target}")
else:
	pass 
if setup.scanHost == "go":
	os.system(f"python3 bucle_host.py -iN {setup.inet} -rG {setup.range}")
else:
	pass
if setup.firtPort == "go":
	os.system(f"python3 fp.py -t {setup.target} -p {setup.port}")
else:
	pass 