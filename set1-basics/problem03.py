#!/usr/bin/env python3

'''
Single-byte XOR cipher
The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
has been XOR'd against a single character. Find the key, decrypt the message.
You can do this by hand. But don't: write code to do it for you.
How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
'''

import set1lib as lib

def main():
    h1 = lib.RawToHex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    topresult = lib.single_char_xor_brute(h1)
    print("------------------")
    print("Top Result:")
    print(topresult)

if __name__ == "__main__":
    main()

