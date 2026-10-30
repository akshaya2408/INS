import numpy as np

key = np.array([[3, 3],
                [2, 5]])
plaintext = input("Enter plaintext: ").upper()
plaintext = plaintext.replace(" ", "")
if len(plaintext) % 2 != 0:
    plaintext += "X"
ciphertext = ""
for i in range(0, len(plaintext), 2):
    a = ord(plaintext[i]) - 65
    b = ord(plaintext[i + 1]) - 65
    p = np.array([[a], [b]])
    c = np.dot(key, p) % 26
    ciphertext += chr(c[0][0] + 65)
    ciphertext += chr(c[1][0] + 65)
print("Encrypted text:", ciphertext)