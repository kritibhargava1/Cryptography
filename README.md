# Cryptography Code Readme

This README file provides an overview of the `cryptograph.py` Python script and its associated files, `stegnography.py` and `codec.py`. This cryptography program allows you to encode and decode messages within images using various encoding methods, including binary, Caesar Cypher, and Huffman Codes.

## `cryptograph.py`

The `cryptograph.py` script is the main program for this cryptography tool. It provides a command-line interface to encode, decode, print, and display images. Below is an overview of the main functions and their usage:

### `main_menu()`
- This function is the main menu for the program.
- It allows you to choose from the following options:
    - E: Encode a message
    - D: Decode a message
    - P: Print a message
    - S: Show an image
    - Q: Quit the program

### `get_message()`
- This function prompts the user to input a message containing only ASCII characters and returns the input.
- It performs a basic check to ensure that the message contains only valid ASCII characters.

### `get_codec()`
- This function allows the user to choose an encoding method from the following options:
    - Steganography only
    - Steganography & Caesar Cypher
    - Steganography & Huffman Codes
    - Return to the main menu

### Execution
- If you run this script as the main program (using `if __name__ == '__main__':`), it will start the main menu, allowing you to use the various functions to perform encoding, decoding, printing, and image display.

## `stegnography.py`

The `stegnography.py` script is responsible for image processing and the steganographic encoding and decoding functions. It includes the following classes and methods:

### `Steganography` Class
- `encode(filein, fileout, message, codec)`: Encodes a message into an image file using the specified codec (binary, Caesar Cypher, or Huffman Codes).
- `decode(filein, codec)`: Decodes a message from an image file using the specified codec.
- `print()`: Prints the text and binary message stored in the class.
- `show(filename)`: Displays the image.

### `Node` Class
- A helper class for implementing a Huffman tree used in `HuffmanCodes`.

### `make_tree(data)`
- Constructs a Huffman tree based on character frequencies in the input data.

### `traverse_tree(node, val)`
- Traverses a Huffman tree, assigning binary codes to leaf nodes.

## `codec.py`

The `codec.py` script contains classes for different encoding methods used in the program:

### `Codec` Class
- `encode(text)`: Converts text into binary form.
- `decode(data)`: Converts binary data into text.

### `CaesarCypher` Class (Inherits from `Codec`)
- `encode(text)`: Converts text into binary form using a Caesar Cipher.
- `decode(data)`: Converts binary data into text using a Caesar Cipher.

### `HuffmanCodes` Class (Inherits from `Codec`)
- `encode(text)`: Converts text into binary form using Huffman Codes (not yet implemented).
- `decode(data)`: Converts binary data into text using Huffman Codes (not yet implemented).

## Running the Program

- To run the program, execute the `cryptograph.py` script.
- Follow the on-screen instructions to encode, decode, print, and display images.

## Example Usage
- An example usage and test cases are provided in the script when run as the main program. You can uncomment the Huffman Codes section and test it if needed.

This README provides a brief overview of the cryptography program and its associated files. You can use this program to perform steganographic encoding and decoding using different encoding methods.
