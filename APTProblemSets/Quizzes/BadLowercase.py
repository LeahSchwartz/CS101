'''
Created on Sep 24, 2017

@author: leahschwartz
'''
def countwords(phrase, cutoff):
    phrase = phrase.split()
    total = 0
    for word in phrase:
        if len(word) > cutoff and word[0] != word[0].upper():
            total = total + 1
    return total
   
    
    
if __name__ == '__main__':
    print countwords("Stranger from within", 4)
