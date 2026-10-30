def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result
text = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))
encrypted_text = caesar_encrypt(text, shift)
print("Encrypted text:", encrypted_text)