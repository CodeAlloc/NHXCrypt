#!/usr/bin/python3
import os, sys

if len(sys.argv) < 3:
	print("Usage: " + sys.argv[0] + " <path to data file> <output file name>")
	exit(2)
try:
	read = open(sys.argv[1], "rb")
except FileNotFoundError:
	print("Error: Specified data file not found")
	exit(-1)
encdec = input("(E)ncrypt/(D)ecrypt: ").lower()
if encdec not in ("d", "e"):
	print("Exitting..")
	exit(-2)
mode = 64
key = input("Enter the Passkey:\t")
if key == "":
	print("Error: No encryption key provided")
	exit(-5)
data = read.read()
write = open(sys.argv[2], "wb")
if encdec == "e":	
	if len(data) < len(key):
		tukey = key[0:len(data)]
	elif len(data) > len(key):
		acc =  int(len(data) / len(key)) + 1
		tukey = key * acc
		tukey = tukey[0:len(data)]
	else:
		tukey = key
	parandom = os.urandom(mode * len(data))
	count = 0
	for char in range(len(data)):			
		if ord(tukey[char]) > (mode - 1):
			stoplength = ord(tukey[char]) - (mode - 1)
		else:
			stoplength = ord(tukey[char])
		temp = []
		for i in range(mode):
			if len(temp) == stoplength - 1:
				write.write(data[char: char + 1])
				temp.append(chr(data[char]))
			else:		
				write.write(parandom[(count*mode) + i : (count*mode) + 1 + i])
				temp.append(parandom[(count*mode) + i])
		count = count + 1
	print("Info: The Encrypted text is written to the file specified.")
elif encdec == "d":
	decbytes = int(len(data) / mode)
	if len(data) % mode != 0:
		print("Error: The encrypted text is corrupted")
		exit(-3)
	if decbytes < len(key):
		tukey = key[0:len(data)]
	elif decbytes > len(key):
		acc =  int(len(data) / len(key)) + 1
		tukey = key * acc
		tukey = tukey[0:len(data)]
	count = 0	
	for char in range(decbytes):
		if ord(tukey[char]) > (mode-1):
			location = ord(tukey[char]) - (mode - 1)
		else:		
			location = ord(tukey[char])
		write.write(data[location + (mode * count) - 1 : location + (mode * count)])
		count = count + 1
	print("Info: The Decrypted text is written to the file specified.")
read.close()
write.close()

