#!/usr/bin/python3
import os, sys

class NHXCrypt:
	def __init__(self, key, mode, readf, writef, verbose=False):		
		self.status = 0
		self.verbose = verbose	
		if os.path.isfile(readf) != True:
			if verbose == True: raise FileNotFoundError("Specified data file not found")
			self.status = 404
		else:
			read = open(readf, "rb")
			self.data = read.read()				
			read.close()
		if mode not in ("8", "16", "32", "64", "128"):
			if verbose == True: raise SystemError("Invalid Mode")
			self.status = 500
		mode = int(mode)
		if key == "":
			if verbose == True: raise SystemError("No Key Given")
			self.status = 505
		self.write = open(writef, "wb")
		self.key = key
		self.mode = mode
	def encrypt(self):
		if self.status != 0:
			return self.status
		data = self.data
		key = self.key
		mode = self.mode
		write = self.write
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
		return 0
	def decrypt(self):
		if self.status != 0:
			return self.status
		data = self.data.decode()
		key = self.key
		mode = self.mode
		write = self.write
		decbytes = int(len(data) / mode)
		if len(data) % mode != 0:			
			if self.verbose == True: raise SystemError("Encrypted File is corrupted/Wrong Mode specified")
			return 600
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
					tudata = chr((ord(tudata) - diff) * -1)
			write.write(tudata.encode("latin"))
			count = count + 1
		return 0
if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: " + sys.argv[0] + " <path to data file> <output file name>")
		exit(2)
	key = input("Enter the Passkey:\t")
	mode = input("Enter the mode (8/16/32/64/128): ")
	encdec = input("(E)ncrypt/(D)ecrypt: ").lower()	
	if encdec == "e":
		status = NHXCrypt(key, mode, sys.argv[1], sys.argv[2]).encrypt()
	elif encdec == "d":
		status = NHXCrypt(key, mode, sys.argv[1], sys.argv[2]).decrypt()
	else:
		print("Exiting...")
		exit(0)
	if status == 404:
		print("Error: Specified Data file doesn't exist")
		exit(status)
	elif status == 500:
		print("Error: Invalid Mode specified")
		exit(status)
	elif status == 505:
		print("Error: No Key Provided")
		exit(status)
	elif status == 600:
		print("Error: Encrypted Text is corrupted or wrong mode is selected")
		exit(status)
	else:
		print("Info: Operation Successful")
