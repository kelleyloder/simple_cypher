# Assignment 5 - Simple Cipher
# Authors: Kelley Loder & Josh Taylor
# Purpose: Allows a user to encipher/decipher messages using a secret word

def encipher(secret_word, plaintext_message):
    """Accepts a secret word and a message, and returns an enciphered message"""
    encode_dictionary = create_encode_dictionary(secret_word)
    new_message = ''
    for letter in plaintext_message:
        if letter.lower() == letter:
            new_message += encode_dictionary.get(letter, letter)
        else:
            new_message += encode_dictionary.get(letter.lower(), letter).upper()
    return new_message

def decipher(secret_word, enciphered_message):
    """Accepts a secret word and a message, and returns a deciphered message"""
    decode_dictionary = create_decode_dictionary(secret_word)
    new_message = ''
    for letter in enciphered_message:
        if letter.lower() == letter:
            new_message += decode_dictionary.get(letter, letter)
        else:
            new_message += decode_dictionary.get(letter.lower(), letter).upper()
    return new_message

def ask_user_task():
    """Asks the user whether they want to encode or decode a phrase,
    and returns their choice"""
    task = raw_input("Would you like to encode or decode a phrase? ")
    task = task.lower()

    while (task != "encode" and (task != "decode")):
        task = raw_input("Please choose 'encode' or 'decode' ")
        task = task.lower()
    
    return task

def ask_user_secret_word():
    """Asks the user what secret word they want to use for creating the cipher,
    and returns their choice"""
    secret_word = raw_input("Please enter a secret word (max 13 characters) ")
    secret_word = secret_word.lower()

    while (not secret_word.isalpha() or len(secret_word) > 13):
        secret_word = raw_input("Secret word must be alphabetic characters" + \
                         " only and less than 13 characters ")
        secret_word = secret_word.lower()
    
    return secret_word

def ask_user_phrase(task):
    """Asks the user what phrase they want to encode/decode"""
    phrase = raw_input("Enter the phrase that you want to " + task + ": ")
    return phrase

def create_encode_dictionary(secret_word):
    """Accepts a secret word and returns a dictionary that maps letters to
    enciphered letters"""
    encode_dictionary = {}
    cipher_list = get_cipher_list(secret_word)
    ndx = 97
    for letter in cipher_list:
        encode_dictionary[chr(ndx)] = letter
        ndx += 1
    return encode_dictionary

def create_decode_dictionary(secret_word):
    """Accepts a secret word and returns a dictionary that maps enciphered
    letters to deciphered letters"""
    decode_dictionary = {}
    cipher_list = get_cipher_list(secret_word)
    ndx = 97
    for letter in cipher_list:
        decode_dictionary[letter] = chr(ndx)
        ndx += 1
    return decode_dictionary
    
def get_cipher_list(secret_word):
    """Accepts a secret word and returns a list used to create a cipher"""
    cipher_list = []
    for letter in secret_word:
        if letter not in cipher_list:
            cipher_list.append(letter)
    length = len(cipher_list)
    ndx = 122
    while len(cipher_list) < 2 * length:
        if chr(ndx) not in cipher_list:
            cipher_list.insert(length, chr(ndx))
        ndx -= 1
    ndx = 97
    while len(cipher_list) < 26:
        if chr(ndx) not in cipher_list:
            cipher_list.append(chr(ndx))
        ndx += 1
    return cipher_list

def ask_user_continue():
    """Asks the user whether they want to continue and returns their choice"""
    user_continue = raw_input("Would you like to continue? ")
    user_continue = user_continue.lower()

    while (user_continue != "yes" and (user_continue != "no")):
        user_continue = raw_input("Please choose 'yes' to continue " + \
                                  "or 'no' to exit ")
        user_continue = user_continue.lower()

    return user_continue == "yes"

def main():
    user_continue = True
    while (user_continue):
        secret_word = ask_user_secret_word()
        task = ask_user_task()    
        phrase = ask_user_phrase(task)
        if task == "encode":
            new_phrase = encipher(secret_word, phrase)
        elif task == "decode":
            new_phrase = decipher(secret_word, phrase)
        print "Here is your", task + "d phrase:"
        print new_phrase
        user_continue = ask_user_continue()

if (__name__ == '__main__'):
    main()
