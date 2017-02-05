import re


def atbash_cipher(code, encode=True):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    splitLength = 5
    codified = ""

    for idx, char in enumerate(code):
        if char.isalpha():
            codified += alpha[-alpha.index(char) - 1]
        else:
            codified += char

        if encode and (idx + 1) % splitLength == 0 and idx and idx != len(code) - 1:
            codified += " "

    return codified


def encode(toEncode):
    toEncode = re.sub(r'\W', '', toEncode).lower()
    return atbash_cipher(toEncode, True)


def decode(encoded):
    return atbash_cipher(encoded.replace(' ', ''), False)
