from string import printable

char_value = {
    'e': 12.702, 't': 9.056, 'o': 7.507, 'a': 8.167, 'i': 6.966,
    'n': 6.749, 's': 6.327, 'h': 6.094, 'r': 5.987, 'd': 4.253,
    'l': 4.025, 'c': 2.782, 'u': 2.758, 'm': 2.406, 'w': 2.360,
    'f': 2.228, 'g': 2.015, 'y': 1.974, 'p': 1.929, 'b': 1.492,
    'v': 0.978, 'k': 0.772, 'j': 0.153, 'x': 0.150, 'q': 0.095,
    'z':0.074, ' ': 15.000
}
    
def xor_with_char(input_bytes, char):
    result = b""

    for byte in input_bytes:
        result += bytes([byte^char])
    
    return result

def xor_bruteforce_with_char(ciphertext):
    
    candidates = []
    
    for char in printable:
        plaintext = xor_with_char(ciphertext, ord(char))
        score = scorer(plaintext)

        candidate = {
            'key': ord(char),
            'score': score,
            'plaintext': plaintext
        }

        candidates.append(candidate)

    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]

def scorer(input_bytes):
    score = 0
    for byte in input_bytes:
        score += char_value.get(chr(byte), 0)
    return score

def print_result(candidate):
    print("Key:" + chr(candidate['key']))
    print("Plaintext:" + str(candidate['plaintext'].rstrip()))
    print("Score:" + str(candidate['score']))


def main():

    ciphertext = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    candidate = xor_bruteforce_with_char(ciphertext)

    print_result(candidate)
            
if __name__ == '__main__':
    main()
