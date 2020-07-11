# NHXCrypt
NHXCrypt is a tool that uses NHXCrypt-8--128 Algorithms to encrypt and decrypt the files using a single key.

  
# Main Features:

  - Support for reading and writing data from and to files (Encryption/Decryption)
  - Using 8, 16, 32, 62 and 128 characters to represent each character to make encryption effective.
  - Easy single key decryption

### Installation

NHXCrypt requires Python 3+ to run.

Download NHXCrypt .py and use it via python3 shell:

```sh
$ python3 NHXHide.py
```

### Usage

Using this tool is simple. One argument is required, which is the image file to read or write data to, and the second optional argument is the file to read the data from, to be written to image, or the file for writng back the extracted data from the image file.

```sh
$ NHXHide <data file: input> <file name for output (overwritten if exixts)>
```
