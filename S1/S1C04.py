from string import printable
from S1C03 import xor_bruteforce_with_char, scorer, print_result

def detect_enc_string(enc_strings):

    candidates = []

    for enc_string in enc_strings:
        candidates.append(xor_bruteforce_with_char(enc_string))

    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]


def main():

    ciphertexts = []

    with open("./4.txt", 'r') as f:
        for hex_string in f.readlines():
            ciphertexts.append(bytes.fromhex(hex_string.rstrip()))

    candidate = detect_enc_string(ciphertexts)
    print_result(candidate)

    print


    #ciphertexts = [bytes.fromhex(line.strip()) for line in open("S1C04_input.txt")]

if __name__ == '__main__':
    main()
    