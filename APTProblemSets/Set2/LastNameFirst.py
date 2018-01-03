'''
Created on Sep 14, 2017

@author: leahschwartz
'''
def modify(name):
    words = name.split()
    firstName = words[0]
    lastName = words[-1]
    middleNames = words[1: ((len(words) -1))]
    if len(words) == 1:
        return firstName
    if len(words) == 2:
        return lastName + ", " + firstName
    else:
        middleLetters =""
        for item in middleNames:
            if len(item) != 1:
                middleLetters = middleLetters + " " + item[0] + "."
            else:
                middleLetters = middleLetters + " " + item[0]
        return lastName +", " + firstName + middleLetters
        
if __name__ == '__main__':
    print modify("Leah Morter M Schwartz")
