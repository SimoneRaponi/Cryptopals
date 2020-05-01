def hex_xor(h1, h2):
    assert(len(h1) == len(h1))
    d1 = int(h1, 16)
    d2 = int(h2, 16)
    xor = d1 ^ d2
    return hex(xor)

def main():
    h1 = "1c0111001f010100061a024b53535009181c"
    h2 = "686974207468652062756c6c277320657965"

    print(hex_xor(h1, h2))

if __name__ == '__main__':
    main()