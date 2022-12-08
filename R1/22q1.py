# added an ecnrypt function
# 110%

cipher_text = input().upper()

def value(char):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters.index(char) + 1


def character(value):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters[value - 1]


def encrypt(text):
    cipher_text = ""
    sum = 0
    for i in range(len(cipher_text)):
        sum += value(cipher_text[i])
        cipher_text += character(sum)
    return cipher_text


def decrypt(cipher_text):
    decyphered_text = ""
    sum = 0
    for i in range(len(cipher_text)):
        decyphered_text += character((value(cipher_text[i]) - sum) % 26)
        sum += value(decyphered_text[i])
    return decyphered_text


print(decrypt(cipher_text))
