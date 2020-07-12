# NHXCrypt
NHXCrypt is a tool that uses NHXCrypt-8--128 Algorithms to encrypt and decrypt the files using a single key.

  
# Main Features:

  - Support for reading and writing data from and to files (Encryption/Decryption)
  - Using 8, 16, 32, 62 and 128 characters to represent each character to make encryption effective.
  - Easy single key decryption

### Installation

NHXCrypt requires Python 3+ to run.

Download [NHXCrypt.py] and use it via python3 shell:

```sh
$ python3 NHXHide.py
```
## How NHXCrypt Encrypts/Decrypts data?

 NHXCrypt uses simple techniques to make encryption possible. Each character in the data file is shuffled between random numbers in accordance with the location corrosponded by the key. Any ASCII character is acceptable as key. If the mode is other than 64 or 128, the key would also alter the original data in order to make it difficult for real data extraction.

### Modes available

The suffix at the end of the name indicates the amount of characters a single character is going to be translated into. The modes include:

* NHXCrypt-8
* NHXCrypt-16
* NHXCrypt-32
* NHXCrypt-64
* NHXCrypt-128

### Usage

Using this tool is simple. One argument is required, which is the image file to read or write data to, and the second optional argument is the file to read the data from, to be written to image, or the file for writng back the extracted data from the image file.

```sh
$ NHXHide <data file: input> <file name for output (overwritten if exixts)>
```

[NHXCrypt.py]: <https://github.com/chmuhammadsohaib/NHXCrypt/NHXCrypt.py>
