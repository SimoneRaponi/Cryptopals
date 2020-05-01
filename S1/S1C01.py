import base64

char_value = {
    'e': 12.702, 't': 9.056, 'o': 7.507, 'a': 8.167, 'i': 6.966,
    'n': 6.749, 's': 6.327, 'h': 6.094, 'r': 5.987, 'd': 4.253,
    'l': 4.025, 'c': 2.782, 'u': 2.758, 'm': 2.406, 'w': 2.360,
    'f': 2.228, 'g': 2.015, 'y': 1.974, 'p': 1.929, 'b': 1.492,
    'v': 0.978, 'k': 0.772, 'j': 0.153, 'x': 0.150, 'q': 0.095,
    'z':0.074, ' ': 15.000
}

def toBase64(hex_string):
    return base64.b64encode(bytearray.fromhex(hex_string)).decode('utf-8')

def main():
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(toBase64(s))

if __name__ == "__main__":
    main()