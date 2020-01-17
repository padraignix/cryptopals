#!/usr/bin/env python3

'''
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.
If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c
after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965
should produce:
746865206b696420646f6e277420706c6179
'''

import set1lib as lib
import binascii

def main():
    
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    print("Str1: " ,s1)
    print("Str2: " ,s2)
    h1 = lib.RawToHex(s1)
    h2 = lib.RawToHex(s2)

    xor = lib.fixedXOR(h1,h2)
    xorstr = binascii.hexlify(xor.encode())
    print("XOR:  " ,xorstr.decode())

if __name__ == "__main__":
    main()

