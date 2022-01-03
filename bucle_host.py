
import os
import time
import datetime
from datetime import datetime
import argparse

global rango

bucle = argparse.ArgumentParser("")
bucle.add_argument('-iN', '--inet', help="inet")
bucle.add_argument('-rG', '--range', help="range")
bucle = bucle.parse_args()
rango = int(bucle.range)
print("Starting shadow 1.0 ", "( https://github.com )", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
for x in range(0, rango):
	os.system(f"python3 hosts.py -t {bucle.inet}{x}")
print("Shadow done: 256 IP addresses (256 hosts up)")