def encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    row = 0
    direction = 1
    for char in text:
        fence[row].append(char)
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    return ''.join(''.join(row) for row in fence)


def decrypt(cipher, rails):
    pattern = list(range(rails)) + list(range(rails - 2, 0, -1))

    positions = [pattern[i % len(pattern)] for i in range(len(cipher))]

    counts = [positions.count(i) for i in range(rails)]

    fence = []
    start = 0

    for count in counts:
        fence.append(list(cipher[start:start + count]))
        start += count

    result = ""
    indexes = [0] * rails

    for pos in positions:
        result += fence[pos][indexes[pos]]
        indexes[pos] += 1

    return result


text = input("Enter text: ")
rails = int(input("Enter number of rails: "))

encrypted = encrypt(text, rails)
print("Encrypted text:", encrypted)

decrypted = decrypt(encrypted, rails)
print("Decrypted text:", decrypted)