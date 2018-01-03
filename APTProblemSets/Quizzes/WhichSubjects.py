'''
Created on Sep 24, 2017

@author: leahschwartz
'''
def isBadCharacter(word):
    total = 0
    for ch in word:
        if ch in "1234567890:- ":
            total = total + 1
    if total >= 1:
        return True
    else:
        return False
        
def computeSubjects(phrase):
    phrase = phrase.split()
    goodWord = []
    for word in phrase:
        if not isBadCharacter(word):
            goodWord.append(word)
    goodWord = " ".join(goodWord)
    goodWord = goodWord.strip()
    return goodWord
            
    
if __name__ == '__main__':
    print computeSubjects("153FS NEUROSCI MW10:05 to11:20 Sec01 Languages207 4989")