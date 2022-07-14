from collections import Counter
import random


def read_file():
    with open('src.txt') as file:#, encoding='utf-8'
        text = file.read()
        freq_table = Counter(text)

    print(freq_table)
    return text, freq_table

def encrypt(text):

    available_letters = list(set(text))
    sub_table = {letter: '' for letter in available_letters}
    enc_text = ''

    for letter in sub_table:
        position = random.randint(0, len(available_letters) - 1)
        sub_letter = available_letters.pop(position)
        sub_table[letter] = sub_letter

    for letter in text:
        enc_text += sub_table[letter]
    return enc_text

def not_cipher( enc_text, freq_table ):
    enc_text_table = Counter(enc_text)
    decrypted = ''

    for sym in enc_text:
        count = enc_text_table[sym]
        for symbol, sym_count in freq_table.items():
            if sym_count == count:
                decrypted += symbol
                break
    return decrypted

def main():
    text, freq_table = read_file()
    encrypted = encrypt(text)
    notencrypt = not_cipher(encrypted, freq_table)
    print(notencrypt)
    return encrypted

if __name__ == '__main__':
    main()