def encode(toEncode):
    """Simple encoding of repeated letters to format: AABBBCCCC to 2A3B4C"""
    encoded = ''
    count = 1
    for index in range(len(toEncode)):
        if index + 1 < len(toEncode) and toEncode[index] == toEncode[index + 1]:
            count += 1
        else:
            if count == 1:
                encoded += toEncode[index]
            else:
                encoded += str(count) + toEncode[index]

            count = 1

    return encoded


def decode(toDecode):
    """Simple decoding of repeated letters to format: 2A3B4C to AABBBCCCC"""
    decoded = ''
    num = ''
    for index in range(len(toDecode)):
        if toDecode[index].isnumeric():
            num += toDecode[index]
        else:
            if num:
                decoded += toDecode[index] * int(num)
            else:
                decoded += toDecode[index]
            num = ''

    return decoded
