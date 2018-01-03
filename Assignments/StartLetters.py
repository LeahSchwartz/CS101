'''
Created on Oct 24, 2017

@author: leahschwartz
'''
def howManyLetters(phrase):
    return len(set([w[0].lower() for w in phrase.split()]))
    
if __name__ == '__main__':
    print howManyLetters("The cat in the hat comes back")