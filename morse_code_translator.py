MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def encode_morse(message):
    encoded_message = ""
    for char in message.upper():
        if char != " ":
            encoded_message += MORSE_CODE_DICT[char] + " "
        else:
            encoded_message += "/ "

    return encoded_message[:-1]

def decode_morse(message):
    decoded_message = ""
    words = message.split("/")

    for word in words:
        chars = word.strip().split(" ")
        for char in chars:
            decoded_message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(char)]
        decoded_message += " "

    return decoded_message[:-1]

def main():
    message = "OpenAI is cool"
    encoded_message = encode_morse(message)
    print(f"Encoded Message: {encoded_message}")

    decoded_message = decode_morse(encoded_message)
    print(f"Decoded Message: {decoded_message}")

if __name__ == '__main__':
    main()
