#!/usr/bin/env python3

'''
Implement PKCS#7 padding
A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. But we almost never want to transform a single block; we encrypt irregularly-sized messages.

One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7.

So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. For instance,

"YELLOW SUBMARINE"
... padded to 20 bytes would be:

"YELLOW SUBMARINE\x04\x04\x04\x04"

###########

https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

'''
import sys
sys.path.insert(1, '../libraries')
import set2lib as lib
from Crypto.Cipher import AES

def main():

    key = b'YELLOW SUBMARINE'
    result = lib.padding_func(key,AES.block_size)
    print(f"{result}")

    result2 = lib.unpadding_func(result,AES.block_size)
    print(f"{result2}")
   
if __name__ == "__main__":
    main()
