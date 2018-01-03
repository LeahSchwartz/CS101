'''
Created on Nov 6, 2017

@author: leahschwartz
'''
def howMany(phrase, letter):
    letterSet = set()
    phraseList = phrase.split()
    for word in phraseList:
        if letter in word.lower():
            letterSet.add(word.lower())
    return len(letterSet)
    
if __name__ == '__main__':
    print howMany("This is a very long long long test of this phrase", "g")