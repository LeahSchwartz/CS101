'''
Created on September 20, 2017
@author: leahschwartz
'''
from StdSuites.Text_Suite import word
from _socket import CAPI

def readFile(fname):
    '''
    returns a list of words read from file
    specified by fname
    '''
    f = open(fname)
    st = f.read()
    f.close()
    return st.split()

def writeFile(words, fname):
    '''
    write every element in words, a list of strings
    to the file whose name is fname
    put a space between every word written, and make
    lines have length 80
    '''
    LINE_SIZE = 80
    f = open(fname,"w")
    wcount = 0
    for word in words:
        f.write(word)
        wcount += len(word)
        if wcount + 1 > LINE_SIZE:
            f.write('\n')
            wcount = 0
        else:
            f.write(' ')
    f.close()

def isVowel(ch):
    #checks if letter is vowel without y
    if ch in "aeiouAEIOU":
        return True
    else:
        return False

def isVowelwithy(ch):
    #checks if letter is vowel with y
    if ch in "aeiouyAEIOUY":
        return True
    else:
        return False   

def isVowelwithoutu(ch): 
    #checks if letter is vowel with y but without u
    if ch in "aeioyAEIOY":
        return True
    else:
        return False
 

def lineToPiglatin(phrase):
    #method returns a string that is piglatin translation of line
    pigList = []
    for word in phrase.split():
        pigList.append(wordToPiglatin(word))
    return " ".join(pigList)

def vowelWordtoPiglatin(word):
    #handles translations for vowel starting words or all consonant words
    if word.upper() != word: #checks if word is not CAPS
        word = word + "-way"
        return word
    else: #handles CAPS words
        word = word + "-WAY"
        return word    
    
    
def wordToPiglatin(word):
    #method returns a string that is piglatin translation of word
    total = 0
    for ch in word: #works on string of all consonants 
        if not isVowelwithy(ch):
            total = total + 1
    if total == len(word):
        word = vowelWordtoPiglatin(word)
        return word
    
    if not isVowel(word[0]): #checks if first letter is vowel
        if (word[0] == "q" or word[0] == "Q") and (word[1] == "u" or word[1] == "U"):
            for ch in word: #handles words starting with qu
                if isVowelwithoutu(ch): #checks if letter is a vowel but not u
                    if word.upper() != word: #checks if word is not CAPS
                            word = word[word.index(ch)] + word[word.index(ch)+1:] + "-" + word[:word.index(ch)] + "ay"
                            word = capitilizeLetter(word)
                            return word
                    else:
                        word = word[word.index(ch)] + word[word.index(ch)+1:] + "-" + word[:word.index(ch)] + "AY"
                        return word
        else:
            for ch in word: #handles words starting with consonant 
                if isVowelwithy(ch) and ch != word[0]: #checks if letter is a vowel inclusive of y
                    if word.upper() != word: #checks if word is not CAPS
                            word = word[word.index(ch)] + word[word.index(ch)+1:] + "-" + word[:word.index(ch)] + "ay"
                            word = capitilizeLetter(word)
                            return word
                    else: #for CAPs consonant words
                        word = word[word.index(ch)] + word[word.index(ch)+1:] + "-" + word[:word.index(ch)] + "AY"
                        return word            
    else: #words starting with vowels
        word = vowelWordtoPiglatin(word)
        return word
    return word

def piglatinToLine(phrase):
    #method returns a string that is English translation of line
    englishList = []
    for word in phrase.split():
        englishList.append(piglatinToWord(word))
    return " ".join(englishList)
    
#
def piglatinToWord(word):
    #method returns a string that is English translation of word
    engWord ="" 
    if word[-4:] == "-way" or word[-4:] == "-WAY": #handles english all consonant and vowel words now ending in way
        engWord = word[:-4]               
        return engWord
    elif word[-5:] == "-quay" or word[-5:] == "-QUAY": #handles english qu words now ending in quay
        engWord = word[word.find("-") + 1: word.find("-") + 3 ] + word[:word.find("-")] 
        engWord = capitilizeLetter(engWord) 
        return engWord
    elif word.upper() == word: #handles english CAPS consonant starting words now ending in ay
        engWord = word[word.find("-") + 1: word.rfind("A")] + word[:word.find("-")]
        return engWord
    else: #handles english consonant words now ending in ay
        engWord = word[word.find("-") + 1: word.rfind("a")] + word[:word.find("-")]
        engWord = capitilizeLetter(engWord)
        return engWord
    return engWord   

        

def capitilizeLetter(engWord):
    #Corrects cap when going back to English
    correctWord = ""
    if engWord.upper() != engWord and engWord.lower() != engWord:
        correctWord = engWord.lower()
        correctWord = correctWord[0].upper() + correctWord[1:]
    else:
        correctWord = engWord
    return correctWord
    
if __name__ == '__main__':
    # start with reading in data file
    filename = "romeo.txt"
    # wordlist is a list of words from the file
    wordlist = readFile(filename)
    print "read",len(wordlist),"words from file",filename 
    
    # result is the file as one long string
    result = ' '.join(wordlist)
    
    # convert to piglatin and write to file
    pigstr = lineToPiglatin(result)
    filenamepig = "pig-" + filename
    writeFile(pigstr.split(),filenamepig)
    print "PIGIFIED " + filename + " written into the file "+ filenamepig
    print "Here are the first 100 characters:"
    print pigstr[0:100]  # just print first 100 chars

   
    # start with reading in data file
    newfilename = "pig-romeo.txt"
    newWordlist = readFile(newfilename)
    print "read", len(newWordlist), "words from file,", newfilename
    
    result = " ".join(newWordlist)
    
    englishstr = piglatinToLine(result)
    newfilenameUnpig = "unpig-" + newfilename
    writeFile(englishstr.split(), newfilenameUnpig)
    print newfilenameUnpig," written into the file "+ newfilename
    print "Here are the first 100 characters:"
    print englishstr[0:100]
