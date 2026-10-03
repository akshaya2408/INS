def encrypt(text, key):
    columns = len(key)
    rows = (len(text) + columns - 1) // columns

    # Add X to fill the matrix
    text = text.ljust(rows * columns, 'X')

    matrix = []
    for i in range(rows):
        matrix.append(text[i * columns:(i + 1) * columns])

    # Read columns according to key order
    result = ""

    for num in sorted(key):
        col = key.index(num)
        for row in matrix:
            result += row[col]

    return result


def decrypt(cipher, key):
    columns = len(key)
    rows = len(cipher) // columns

    matrix = [[''] * columns for _ in range(rows)]

    index = 0

    # Fill columns according to key order
    for num in sorted(key):
        col = key.index(num)

        for row in range(rows):
            matrix[row][col] = cipher[index]
            index += 1

    # Read row by row
    result = ""
    for row in matrix:
        result += ''.join(row)

    return result.rstrip('X')


key = [3, 1, 4, 2]

text = input("Enter plaintext: ").replace(" ", "").upper()

encrypted = encrypt(text, key)
print("Encrypted text:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted text:", decrypted)