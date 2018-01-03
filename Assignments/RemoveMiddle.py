'''
Created on Sep 12, 2017

@author: leahschwartz
'''
def shorten(name):
    wordsInName = name.split()
    firstName = wordsInName[0]
    lastName = wordsInName[-1]
    if len(wordsInName) == 1:
        return firstName
    else:
        return firstName + " " + lastName
if __name__ == '__main__':
    print shorten("Leah")