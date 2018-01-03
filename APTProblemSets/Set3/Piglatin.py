'''
Created on Sep 19, 2017

@author: leahschwartz
'''
def isVowel(ch):
    if ch in "aeiou":
        return True
    else:
        return False
    
def convert(s):
    if isVowel(s[0]):
            s = s + "-way"    
            return s    
    elif s[0] == "q":
        s = s[2:] + "-" + s[0:2] + "ay"
        return s
    else:
        for letter in s:
            if isVowel(letter):
                s = s[s.index(letter):] + "-" + s[:s.index(letter)] + "ay"
                return s 
        
        
if __name__ == '__main__':
    print convert("crater")