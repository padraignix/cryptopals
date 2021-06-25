#!/usr/bin/env python3

'''
The Base64-encoded content in this file has been encrypted via AES-128 in ECB mode under the key

"YELLOW SUBMARINE".
(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all.

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.

Do this with code.
You can obviously decrypt this using the OpenSSL command-line tool, but we're having you get ECB working in code for a reason. You'll need it a lot later on, and not just for attacking ECB.

###########

https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

'''

import base64
import binascii
import sys
sys.path.insert(1, '../libraries')
import set1lib as lib

def main():

    f = open("data07.txt", "r")
    ciphertext = ''.join(f.read().strip().split('\n'))
    f.close()

    #print(f"{ciphertext}")
    
    key = b'YELLOW SUBMARINE'
    plaintext = lib.aes_cbc_decode(key, ciphertext, "pkcs7", 16)
    
    print(f"{plaintext}")

if __name__ == "__main__":
    main()

