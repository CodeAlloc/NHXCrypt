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
mode = input("Enter the mode (8/16/32/64/128): ")
if mode not in ("8", "16", "32", "64", "128"):
	print("Error: Invalid Mode")
	exit(5)
mode = int(mode)
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
		tudata = ord(data[char: char + 1])		
		if mode < 64:
			if ord(tukey[char]) > (mode - 1):
				keyval = ord(tukey[char])
				acc = keyval - mode
				while acc > (mode - 1):
					 acc = int(acc) / 2
				stoplength = int(acc)
				diff = keyval - int(acc)
				tudata = tudata + diff
			else:
				stoplength = ord(tukey[char])
		else:
			if ord(tukey[char]) > (mode - 1):
				stoplength = ord(tukey[char]) - (mode - 1)
			else:
				stoplength = ord(tukey[char])
		temp = 0
		for i in range(mode):
			if temp == stoplength - 1:
				write.write(chr(tudata).encode())
				temp = temp + 1
			else:
				write.write(chr(parandom[(count*mode) + i]).encode())
				temp = temp + 1
		count = count + 1
	print("Info: The Encrypted data is written to the file specified.")
elif encdec == "d":
	data = data.decode()
	decbytes = int(len(data) / mode)
	if len(data) % mode != 0:
		print("Error: Incorrect mode or the encrypted file is corrupted")
		exit(-3)
	if decbytes < len(key):
		tukey = key[0:len(data)]
	elif decbytes > len(key):
		acc =  int(len(data) / len(key)) + 1
		tukey = key * acc
		tukey = tukey[0:len(data)]
	count = 0	
	for char in range(decbytes):
		diff = 0
		if mode < 64:
			if ord(tukey[char]) > (mode - 1):
				keyval = ord(tukey[char])
				acc = keyval - mode
				while acc > (mode - 1):
					 acc = int(acc) / 2
				location = int(acc)
				diff = keyval - int(acc)
			else:
				location = ord(tukey[char])
		else:
			if ord(tukey[char]) > (mode-1):
				location = ord(tukey[char]) - (mode - 1)
			else:		
				location = ord(tukey[char])
		tudata = data[location + (mode * count) - 1 : location + (mode * count)]
		if diff != 0:
			try:
				tudata = chr(ord(tudata) - diff)
			except ValueError:
				print("Error: Incorrect Mode/Password caused crash during value altering")
				exit(404)
		write.write(tudata.encode("latin"))
		count = count + 1
	print("Info: The Decrypted data is written to the file specified.")
read.close()
write.close()

