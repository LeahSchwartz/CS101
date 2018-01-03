'''
Created on Sep 24, 2017

@author: leahschwartz
'''
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
            f.write('')
    f.close()
    
def encrypt(str, shift):
    answer = []
    for word in str.split():
        answer.append(encryptword(word, shift))
    return " ".join(answer)

def encryptword(word, shift):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #word = word.upper()
    alphlow = "abcdefghijklmnopqrstuvwxyz"
    caesar = alph[shift:] + alph[:shift]
    caesarlow = alphlow[shift:] + alphlow[:shift]
    newWord = ""
    letterIndex = 0  
    for ch in word:
        if ch.isalpha():
            if ch == ch.upper():
                findex = alph.find(ch)
                newWord = newWord + caesar[findex]
            else:
                findex = alphlow.find(ch)
                newWord = newWord + caesarlow[findex]
        else:
            newWord = newWord + ch 
    return newWord 

def eyeball(encrypted):
    for number in range(0, 26):
        print number, encrypt(encrypted, number)[0:80]
        
def decrypt(encrypted):
    shiftLines = []
    runningTally = 0
    probItem = ""
    englishWords = readFile("melville.txt")
    for number in range(1, 26):
        shiftLines.append(encrypt(encrypted, number))
    for item in shiftLines:
        tally = 0
        for word in item.split():
            if word.lower() in englishWords:
                tally = tally + 1
                if tally > runningTally:
                    runningTally = tally
                    probItem = item   
    return probItem
 
if __name__ == '__main__':
    filename = "melville.txt"
    print "Reading and making a list of words from the file " + filename
    wordList = readFile(filename)
    result = " ".join(wordList)
    print "Converting list of words from " + filename + " into a string"
    encryptstr = encrypt(result, 4) 
    print "Encrypting " + filename
    filenameEncrypt = "encrypt" + filename
    writeFile(encryptstr, filenameEncrypt)
    print "Writing encrypted version of " + filename + " into file " + filenameEncrypt
     
    newWordList = readFile(filenameEncrypt)
    print "Reading and making a list of words from the file " + filenameEncrypt
    newResult = " ".join(newWordList)
    print "Converting list of words from " + filenameEncrypt + " into a string"
    print "The next part may take a while. ~Please wait~"
    decrypstr = decrypt(newResult)
    print "Decrypting " + filenameEncrypt
    filenameDecrypt = "unencr-" + filenameEncrypt
    writeFile(decrypstr, filenameDecrypt)
    print "Writing decrypted version of " + filenameEncrypt + " into file " + filenameDecrypt
    print "Running eyeball decryption on " + filenameEncrypt + " and printing the first 80 characters (spot the correct line!):"
    eyeball(newResult)
    
    
