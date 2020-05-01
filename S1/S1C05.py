import binascii


def repeating_key_xor(plaintext, key):
        ciphertext = b''
        i = 0

        for char in plaintext:
            ciphertext += bytes([char ^ key[i]])
            
            if i < len(key) - 1:
                i += 1
            else:
                i = 0
                
        return ciphertext

def main():

    plaintext = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'

    print(str(binascii.hexlify(repeating_key_xor(plaintext, key)), "utf-8"))

if __name__ == '__main__':
    main()
    