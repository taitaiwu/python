from Crypto.Cipher import AES


key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
iv = bytes.fromhex("00000000000000000000000000000000")
test_data = [
    ("00000000000000000000000000000000", "00000000000000000000000000000001"),
    ("0123456789abcdeffedcba9876543210", "0023456789abcdeffedcba9876543210"),
    ("0e3634aece7225b6f26b174ed92b5588", "0f3634aece7225b6f26b174ed92b5588"),
    ("657470750fc7ff3fc0e8e8ca4dd02a9c", "c4a9ad090fc7ff3fc0e8e8ca4dd02a9c"),
    ("5c7bb49a6b72349b05a2317ff46d1294", "fe2ae569f7ee8bb8c1f5a2bb37ef53d5"),
    ("7115262448dc747e5cdac7227da9bd9c", "ec093dfb7c45343d689017507d485e62"),
    ("f867aee8b437a5210c24c1974cffeabc", "43efdb697244df808e8d9364ee0ae6f5"),
    ("721eb200ba06206dcbd4bce704fa654e", "7b28a5d5ed643287e006c099bb375302"),
    ("0ad9d85689f9f77be1c5f71185e5fb14", "3bce2d8b6798d8ac4fe36a1d891ac181"),
    ("db18a8ffa16d30d5f788b08d777ba4ea", "9fb8b5452023c70280e5c4bb9e555a4b"),
    ("f91b4fbfe934c9bf8f2f85812b084989", "20264e1126b219aef7feb3f9b2d6de40"),
    ("cca104a13e678500ff59025f3bafaa34", "b56a0341b2290ba7dfdfbddcd8578205"),
    ("ff0b844a0853bf7c6934ab4364148fb9", "612b89398d0600cde116227ce72433f0"),
]

def encrypt(plaintext_hex):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(bytes.fromhex(plaintext_hex))

def hamming_distance(b1, b2):
    return sum(bin(x ^ y).count('1') for x, y in zip(b1, b2))

total = 0

for i, (p1, p2) in enumerate(test_data, 1):
    c1 = encrypt(p1)
    c2 = encrypt(p2)

    diff = hamming_distance(c1, c2)
    percent = diff / 128 * 100

    print(f"[Test {i}]")
    print("P1:", p1)
    print("P2:", p2)
    print("C1:", c1.hex())
    print("C2:", c2.hex())
    print(f"Bit differences: {diff}")
    print(f"Percentage: {percent:.2f}%")
    print("-" * 40)
