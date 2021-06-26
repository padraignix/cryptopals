import base64
from Crypto.Cipher import AES
from Crypto.Util import Padding
import itertools

def padding_func(data, size_b):
    data_padded = Padding.pad(data, size_b)
    return data_padded

def unpadding_func(data, size_b):
    data_unpadded = Padding.unpad(data, size_b)
    return data_unpadded

def aes_ecb_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)

def aes_ecb_decrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)

def aes_cbc_encrypt(key, plaintext, iv):
    prev_b = iv
    ciphertext = b''
    padded_plain = padding_func(plaintext, AES.block_size)
    for i in range(0, len(padded_plain), AES.block_size):
        #print (f"{plaintext[i:i+AES.block_size]}")
        block = padded_plain[i:i+AES.block_size]
        #print (f"{block}")
        xor_b = bytes([b1 ^ b2 for b1, b2 in zip(block, prev_b)])
        encrypted_b = aes_ecb_encrypt(xor_b,key)
        #print (f"{encrypted_b}")
        ciphertext += encrypted_b
        prev_b = encrypted_b
    return ciphertext

def aes_cbc_decrypt(key, ciphertext, iv):
    prev_b = iv
    plaintext = b''
    for i in range(0, len(ciphertext), AES.block_size):
        block = ciphertext[i:i+AES.block_size]
        #print (f"{block}")
        decrypt_b = aes_ecb_decrypt(block,key)
        xor_b = bytes([b1 ^ b2 for b1, b2 in zip(prev_b,decrypt_b)])
        plaintext += xor_b
        prev_b = block
    return unpadding_func(plaintext, AES.block_size)