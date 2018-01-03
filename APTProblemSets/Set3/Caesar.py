'''
Created on Sep 19, 2017

@author: leahschwartz
'''
def decode(cipher,shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newLetter = ""
    for letter in cipher:
        newLetter = newLetter + alphabet[alphabet.find(letter) - shift]
    return newLetter
if __name__ == '__main__':
    print decode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4)