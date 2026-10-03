def encrypt(text, key):
    text = text.replace(" ", "").upper()
    n = len(key)

    # Add X to fill the matrix
    while len(text) % n != 0:
        text += "X"

    # Create matrix row-wise
    matrix = []
    for i in range(0, len(text), n):
        matrix.append(text[i:i+n])

    # Read columns according to sorted key
    result = ""

    for k in sorted(key):
        col = key.index(k)

        for row in matrix:
            result += row[col]

    return result


def decrypt(cipher, key):
    n = len(key)
    rows = len(cipher) // n

    matrix = [[''] * n for _ in range(rows)]

    index = 0

    # Fill columns according to key order
    for k in sorted(key):
        col = key.index(k)

        for row in range(rows):
            matrix[row][col] = cipher[index]
            index += 1

    # Read row-wise
    result = ""

    for row in matrix:
        result += ''.join(row)

    return result.rstrip("X")


key = [3, 1, 4, 2]

text = input("Enter plaintext: ")

encrypted = encrypt(text, key)
print("Encrypted text:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted text:", decrypted)