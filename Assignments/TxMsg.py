'''
Created on Sep 21, 2017

@author: leahschwartz
'''
def getMessage(original):
    ret = ""
    for word in original.split():
        ret = ret + " " + transform(word)
    ret = ret.strip()
    return ret
    
def isVowel(l):
    if l in "aeiou":
        return True
    else:
        return False
#if vowels equals length of string do nothing
def transform(word):
    answer = ""
    before = "a"
    total = 0
    for ch in word:
        if isVowel(ch):
            total = total + 1
        if total == len(word):
            answer = word
            return answer
    if len(word) == 1:
        answer = word
    else:
        for ch in word:    
            if isVowel(before) and not isVowel(ch):
                answer = answer + ch 
            before = ch
    return answer

    
if __name__ == '__main__':
    print getMessage("text message")