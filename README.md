# Morse Code Translator

This is a simple Morse Code Translator written in Python. This program can convert text to Morse code and vice versa.

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
- [Contribute](#contribute)
- [Contact](#contact)

## Installation

Clone the repository using the following command:

```bash
git clone https://github.com/sonnymay/morse-code-translator.git
```

Change directory:

```bash
cd morse-code-translator
```

Ensure that you have Python installed on your machine. You can download it [here](https://www.python.org/downloads/).

## Usage

You can run the program using the following command:

```bash
python morse_code_translator.py
```

To encode a message to Morse code, call the `encode_morse` function:

```python
message = "OpenAI is cool"
encoded_message = encode_morse(message)
print(f"Encoded Message: {encoded_message}")
```

To decode a Morse code message, call the `decode_morse` function:

```python
decoded_message = decode_morse(encoded_message)
print(f"Decoded Message: {decoded_message}")
```

## Contribute

If you want to contribute to this project, please feel free to fork the repository, make some changes, and open a pull request. All contributions are welcome.
