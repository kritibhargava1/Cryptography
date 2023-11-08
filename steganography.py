# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        print(image) # for debugging
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message+self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes < max_bytes:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary
            encode = cv2.imread(filein)
            last_bit,row, col  = encode[-1],0, 0
            bool = False
            binary1 = self.binary
            for i in last_bit:
                for j in i:
                    if len(binary1) == 0:
                        bool = True
                    elif int(binary1[0]) % 2 != 0 and int(j) % 2 == 0:
                        last_bit[row][col] = str(int(last_bit[row][col]) + 1)
                    elif int(binary1[0]) % 2 == 0 and int(j) % 2 != 0:
                        last_bit[row][col] = str(int(last_bit[row][col]) - 1)
                    
                    col += 1
                    binary1 = binary1[1:]
                row += 1
                col = 0
            encode[-1] = last_bit
            cv2.imwrite(fileout, encode)
            
        else:
            print("Error: Insufficient bytes!")
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        #print(image) # for debugging      
        flag = True
        
        # convert into text
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            last_bit = image[-1]
            bin = ''
            cur = ''
            bool = False
            for i in last_bit:
                for j in i:
                    if int(j) % 2 == 0:
                        cur += "0"
                    elif int(j) % 2 != 0:
                        cur += "1"
                    if len(cur) == 8:
                        bin += cur
                        if self.codec.decode(cur) == "":
                            bool = True
                            break
                        cur = ""
            binary_data = bin
            # your code goes here
            # you may create an additional method that extract bits from the image array
            #pass
            #binary_data = ?
            # update the data attributes:
            self.text = self.codec.decode(binary_data)
            self.binary = binary_data            
        
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

if __name__ == '__main__':
    
    s = Steganography()

    s.encode('fractal.jpg', 'fractal.png', 'hello', 'binary')
    # NOTE: binary should have a delimiter and text should not have a delimiter
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'

    s.decode('fractal.png', 'binary')
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'
    print('Everything works!!!')
   
