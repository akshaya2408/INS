def create_matrix(key):
    key = key.upper().replace("J", "I")
    letters = ""

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in letters:
            letters += ch
    matrix = [letters[i:i+5] for i in range(0, 25, 5)]
    return matrix
def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
def encrypt(text, key):
    matrix = create_matrix(key)
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())
    # Make pairs
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 == len(text):
            b = "X"
            i += 1
        elif text[i] == text[i + 1]:
            b = "X"
            i += 1
        else:
            b = text[i + 1]
            i += 2
        pairs.append(a + b)
    result = ""
    # Encryption
    for pair in pairs:
        a, b = pair
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result
key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

print("Encrypted text:", encrypt(plaintext, key))