#!/usr/bin/env python3

'''
Detect single-character XOR
One of the 60-character strings in this file (data04.txt) has been encrypted by single-character XOR.
Find it.
(Your code from #3 should help.)
'''
import binascii
import set1lib as lib

def main():
    datafile = open("data04.txt", "r")
    currentscore = 0
    candidate = []
    currentline = 0
    finalline = 0
    ciphertext = ''

    for line in datafile:
        currentline += 1
        h1 = lib.RawToHex(line.rstrip())
        topresult = lib.single_char_xor_brute(h1)
        if topresult['score'] > currentscore:
            currentscore = topresult['score']
            candidate = topresult
            finalline = currentline
            ciphertext = line

    print("Line: ", finalline, "- Ciphertext: ", ciphertext.rstrip())
    key = str(candidate['key'])
    keyascii = binascii.unhexlify(key)
    print("Key:" , keyascii.decode())
    print(candidate)

if __name__ == "__main__":
    main()

