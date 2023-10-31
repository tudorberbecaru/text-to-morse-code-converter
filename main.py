from bidict import bidict
from itertools import groupby

# Define Morse code dictionary
MORSE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': ' ',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '!': '-.-.--',
    ';': '-.-.-.',
    ':': '---...',
    "'": '.----.',
    '-': '-....-',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '_': '..--.-'
}

# Create an inverse dictionary for decoding
MORSE_DICT_INVERSE = bidict(MORSE_DICT).inverse


# Function to encode text to Morse code
def encode(text):

    split_words = text.split(" ")  # Split the input text into words
    encoded_text = ''
    words_to_encode = []

    for word in split_words:
        word_chars = list(word)  # Split each word into characters
        words_to_encode.append(word_chars)  # Store characters for each word

    for word_index, word in enumerate(words_to_encode):
        for letter_index, letter in enumerate(word):
            if letter.upper() in MORSE_DICT:
                encoded_text += (MORSE_DICT[letter.upper()])  # Encode the letter
            else:
                encoded_text += "#"  # Handle untranslatable characters with '#'
            if letter_index != len(word) - 1:
                encoded_text += " "  # Add space between letters in the same word
        if word_index != len(words_to_encode) - 1:
            encoded_text += " / "  # Add a slash between words

    return encoded_text


# Function to decode Morse code to text
def decode(text):

    split_text = text.split(" ")
    morse_code_chars = [list(g) for k, g in groupby(
        split_text, lambda x: x == "/")]  # Split Morse code characters by '/'
    decoded_text = ''

    for element in morse_code_chars:
        if element == ['/']:
            decoded_text += " "  # Handle spaces between words
        else:
            for char in element:
                try:
                    decoded_text += MORSE_DICT_INVERSE[char]  # Decode the Morse code character
                except KeyError:
                    raise ValueError('Invalid Morse code.')  # Handle invalid Morse code

    return decoded_text


if __name__ == "__main__":

    print(
        """
MORSE CODE ENCODER/DECODER
This is a text-based Python program that allows you to encode or decode Morse code.

Use '.' and '-' for Morse code
Use ' ' to separate letters
Use '/' to separate words
'#' denotes an untranslatable character
        """
    )

    while True:
        mode = input("Do you want to encode ('e') or decode ('d') Morse code?: ")

        if mode == "e":
            message = input("Mode: ENCODING\n\nType text: ")
            result = encode(message)
            print(result + "\n")

        elif mode == "d":
            message = input("Mode: DECODING\n\nType Morse code: ")
            try:
                result = decode(message)
                print(result + "\n")
            except ValueError as e:
                print(str(e))
        else:
            print("Invalid mode. Please choose 'e' for encoding or 'd' for decoding.\n")

        another_action = input("Do you want to perform another action? (y/n): ")
        if another_action.lower() != "y":
            break
