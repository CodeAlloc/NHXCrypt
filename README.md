# NHXCrypt
NHXCrypt is a tool that uses NHXCrypt-8--128 Algorithms to encrypt and decrypt the files using a single key.

  
# Main Features:
  - Support for reading and writing data from and to files (Encryption/Decryption)
  - Using 8, 16, 32, 62 and 128 characters to represent each character to make encryption effective.
  - Easy single key decryption

## How NHXCrypt Encrypts/Decrypts data?

 NHXCrypt uses simple techniques to make encryption possible. Each character in the data file is shuffled between random numbers in accordance with the location corrosponded by the key. Any ASCII character is acceptable as key. If the mode is other than 64 or 128, the key would also alter the original data in order to make it difficult for real data extraction.

### Modes available

The suffix at the end of the name indicates the amount of characters a single character is going to be translated into. The modes include:

* NHXCrypt-8
* NHXCrypt-16
* NHXCrypt-32
* NHXCrypt-64
* NHXCrypt-128
### Installation

NHXCrypt requires Python 3+.
To use it as a module, install NHXCrypt using pip:
```sh
pip3 install NHXCrypt
```

To use it as a tool, Download: [NHXCrypt.py] and use it via python3 shell:

```sh
$ python3 NHXCrypt.py
```
or in Linux or MacOS, directly as:
```sh
$ git clone https://www.github.com/chmuhammadsohaib/NHXCrypt
$ cd NHXCrypt
$ chmod +x NHXCrypt.py
$ ./NHXCrypt0
```

### Usage

Using NHXCrypt as a tool is simple. One argument is required, which is the image file to read or write data to, and the second optional argument is the file to read the data from, to be written to image, or the file for writng back the extracted data from the image file.

```sh
$ NHXHide <data file: input> <file name for output (overwritten if exixts)>
```

To use it as a module, simply use it as follows:

```sh
import NHXCrypt

handler = NHXCrypt.NHXCrypt(<key>, <mode>, <file name to encrypt>, <file name to output the encrypted data [overwritten if exists]>, verbose=<True/False [default=False]>)
```
For Encrypting, type:
```sh
handler.encrypt()
```

To Decrypt, type:
```sh
handler.decrypt()
```

When verbose is set to True, an exception is raised rather than providing a status code. By default, a status code would be provided which can be used to raise exceptions in custom way, for example:
```
status = handler.decrypt()
if status == 0:
        print("Success")
```

There are 6 different status codes:

| Status Code | Meaning |
|---------|-----------|
|0| Operation Successful
|404| Data File not Found
|500| Invalid Mode
|505| No Key provided
|600| Encrypted Text corrupted or wrong mode selected

Found NHXCrypt interesting? Go and Install it with just some simple steps!

[NHXCrypt.py]: <https://github.com/chmuhammadsohaib/NHXCrypt/blob/master/NHXCrypt/NHXCrypt.py>

