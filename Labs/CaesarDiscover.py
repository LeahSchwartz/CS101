'''
Created on Nov 8, 2017

@author: leahschwartz
'''
import SimpleCaesar
from SimpleCaesar import encrypt

def textToWords(filename):
    wordList = set()
    f = open(filename)
    for line in f:
        line = line.strip()
        wordList.add(line)
    return wordList  

def shiftedWords(wordList):
    returnList = []
    count = 0
    for num in range(1,26):
        for word in wordList:
            newWord = encrypt(word, num)
            if newWord in wordList:
                print num, word, newWord
                count += 1
    print "there are", count, "pairs"

if __name__ == '__main__':
    wordList = textToWords("lowerwords.txt")
    print shiftedWords(wordList) 
