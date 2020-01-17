import base64

#English language character frequency analysis
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def hexToBase64(s):
    hexstr = bytes.fromhex(s)
    b64 = base64.b64encode(hexstr)
    return b64.decode()

def strToBase64(s):
    b64 = base64.b64encode(s)
    return b64.decode()

def RawToHex(s):                                                                                                                                                 
    h = bytes.fromhex(s)
    return h                      

def fixedXOR(h1, h2):
    result = ''
    for x,y in zip(h1,h2):
        result += chr(x ^ y)
    return result

def singlecharXOR(h1, k1):
    result = ''
    for x in h1:
        result += chr(x ^ k1)
    return result

def repeatkeyXOR(h1, k1):
    result = b''
    count = 0
    for x in h1:
        result += bytes([x ^ k1[count]])
        count += 1
        if count >= len(k1):
            count = 0
    return result

def get_freq_score(p1):
    score = 0
    for byte in p1:
        score += CHARACTER_FREQ.get(byte.lower(), 0)
    return score

def single_char_xor_brute(c1):

    currentscore = 0

    for key in range(256):
        p1 = singlecharXOR(c1, key)
        score = get_freq_score(p1)

        result = {
            'key': key,
            'score': score,
            'plaintext': p1
        }

        if result['score'] > currentscore:
            top = result
            currentscore = result['score']

    return top

def hamming_dist(s1, s2):
    distance = 0
    xor_bytes = [b1 ^ b2 for b1,b2 in zip(s1,s2)]
    for byte in xor_bytes:
        distance += sum([1 for bit in bin(byte) if bit == '1'])
    return distance

def key_size_determine(data):
    keysize_list = []
    chunk_size=2
    while chunk_size <= 40: 
        chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
        distincr = 0
        i = 0 
        while i < len(chunks) - 1:
            distincr += hamming_dist(chunks[i], chunks[i+1]) / chunk_size
            i += 2
        dist = distincr / (len(chunks) / 2)

        iteration = {
            'key_size': chunk_size,
            'score': dist,
        }
        keysize_list.append(iteration)
        chunk_size += 1
    topchoice = sorted(keysize_list, key=lambda x: x['score'])
    return topchoice[0]['key_size']

def determine_key_based_on_len(candidate_size, data):
    key = b''
    for i in range(candidate_size):
        block = b''
        for j in range(i,len(data),candidate_size):
            block += bytes([data[j]])
        topres = single_char_xor_brute(block)
        key += chr(topres['key']).encode()
    return key
