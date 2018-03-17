def is_char_between_letters(char, start, end):
    return ord(start) <= ord(char) and ord(char) <= ord(end)


def ceasar_cypher(text, offsetLetter):
    offset = 0
    if (is_char_between_letters(offsetLetter, 'A', 'Z')):
        offset = ord(offsetLetter) - ord('A')
    elif (is_char_between_letters(offsetLetter, 'a', 'z')):
        offset = ord(offsetLetter) - ord('a')

    result = ''
    for letter in text:
        encrypted = None
        if is_char_between_letters(letter, 'A', 'Z'):
            encrypted = (((ord(letter) - ord('A')) + offset) % 26) + ord('A')
        elif is_char_between_letters(letter, 'a', 'z'):
            encrypted = (((ord(letter) - ord('a')) + offset) % 26) + ord('a')
        else:
            encrypted = letter

        result += str(chr(encrypted))
    return result


def vigenere_cyper(text, key):
    result = ''
    keyIndex = 0
    for letter in text:
        result += ceasar_cypher(letter, key[keyIndex])
        keyIndex = (keyIndex + 1) % len(key)
    return result


text = 'ATTACKATDAWN'
key = 'LEMON'

print(vigenere_cyper(text, key))