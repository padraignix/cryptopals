#!/usr/bin/env python3

'''
Detect AES in ECB mode
In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

###########

https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

'''
import sys
sys.path.insert(1, '../libraries')
import set1lib as lib

def main():

    f = open("data08.txt", "r")
    ciphertexts = [bytes.fromhex(line.strip()) for line in f]
    f.close()

    result = lib.determine_aes_ecb(ciphertexts,16)
    print(f"{result}")
   
if __name__ == "__main__":
    main()
