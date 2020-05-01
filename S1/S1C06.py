from itertools import combinations
from S1C03 import xor_bruteforce_with_char, scorer
from S1C05 import repeating_key_xor
from base64 import b64decode

''' Computes the Hamming distance between two equal-length strings'''
def hamming_distance(binary1, binary2):
    assert(len(binary1) == len(binary2))

    distance = 0

    for b1, b2 in zip(binary1, binary2):
        distance += str(bin(b1^b2)).count('1')

    return distance

def break_repeating_key_xor(binary):
    distances = {}
    k_size_attempts = 3
    k_size_worth = 4
    denominator = 6

    for k_size in range(2, 41):
        temp_chunks = [binary[i:i+k_size] for i in range(0, len(binary), k_size)][:k_size_worth]
        distance = 0
        chunks = combinations(temp_chunks, 2)
        for (x,y) in chunks:
            distance += hamming_distance(x,y)

        distance /= denominator
        distances[k_size] = distance / k_size

    candidates_plaintexts = []
    candidates_k_sizes = sorted(distances, key=distances.get)[:k_size_attempts]


    for candidate_k_size in candidates_k_sizes:
        key = b''
        for block_index in range(candidate_k_size):
            b = b''
            for i in range(block_index, len(binary), candidate_k_size):
                b += bytes([binary[i]])

            candidate = xor_bruteforce_with_char(b)
            key += bytes([candidate['key']])

        candidates_plaintexts.append((repeating_key_xor(binary, key), key))

    return max(candidates_plaintexts, key=lambda k: scorer(k[0]))

def print_result(result):
    
    plaintext = result[0].decode().rstrip()
    key = result[1].decode()

    print("Key:" + key)
    print("Plaintext:" + plaintext)

def main():
    string1 = b'this is a test'
    string2 = b'wokka wokka!!!'

    print(hamming_distance(string1, string2))

    with open("6.txt") as f:
        decoded_data = b64decode(f.read())
        result = break_repeating_key_xor(decoded_data)
        print_result(result)
        


if __name__ == '__main__':
    main()
    