#!/usr/bin/env python3

'''
Implement CBC mode
CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block cipher natively only transforms individual blocks.

In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.

The first plaintext block, which has no associated previous ciphertext block, is added to a "fake 0th ciphertext block" called the initialization vector, or IV.

Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), and using your XOR function from the previous exercise to combine them.

The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)

Don't cheat.
Do not use OpenSSL's CBC code to do CBC mode, even to verify your results. What's the point of even doing this stuff if you aren't going to learn from it?

###########

https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

'''
import sys
sys.path.insert(1, '../libraries')
import set1lib as lib1
import set2lib as lib2
from Crypto.Cipher import AES
import base64

def main():

    
    key = b'YELLOW SUBMARINE'
    plaintext = b'This is a test text message going to see if it works'
    iv = b'\x00' * AES.block_size
    
    #Test encrypt
    print(f"{plaintext}\n")
    result = lib2.aes_cbc_encrypt(key,plaintext,iv)
    print(f"{result}\n")

    #Test decrypt
    result2 = lib2.aes_cbc_decrypt(key,result,iv)
    print(f"{result2}\n")
    
    #Decrypt provided data
    f = open("data10.txt", "r")
    read = ''.join(f.read().strip().split('\n'))
    f.close()
    ciphertext = base64.b64decode(read)
    result3 = lib2.aes_cbc_decrypt(key,ciphertext,iv)
    print(f"{result3}\n")
   
if __name__ == "__main__":
    main()
