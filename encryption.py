english_words = []


def encrypt(message, key):
    message = message.lower()
    key %= 26
    cipher = ""
    for letter in message:
        if letter < 'a' or letter > 'z':
            cipher += letter
        else:
            cipher += chr((ord(letter) + key - 97) % 26 + 97)

    return cipher


def decrypt(cipher):
    best = 0
    message = ""
    key = 0
    for i in range(0, 26):
        decoded = encrypt(cipher, i)
        words = decoded.split()
        length = len(words)
        match = 0
        for word in words:
            if word in english_words:
                match += 1

        point = match/length*100

        if best < point:
            best = point
            message = decoded
            key = 26 - i

    if best >= 70:
        return message + ", key=" + str(key)
    else:
        return "Unsolvable!!"


def make_dictionary():
    file = open("google-10000-english.txt", "r")
    for line in file:
        english_words.append(line.strip())
    file.close()


make_dictionary()

cipher_text = raw_input("please enter ciphered text here:")
print("result:\n" + decrypt(cipher_text))
