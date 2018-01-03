'''
Created on Sep 24, 2017

@author: leahschwartz
'''
def countVowelWords(phrase):
    total = 0
    phrase = phrase.split()
    for word in phrase:
        if isVowel(word[0]) and isVowel(word[-1]):
            if word[0] != word[-1]:
                total = total + 1
    return total
  
def isVowel(ch):
    if ch in "aeiou":
        return True
    else:
        return False
       
if __name__ == '__main__':
    print countVowelWords("usa will unite the entire world")