'''
Created on Sep 19, 2017

@author: leahschwartz
'''
def decode(phrase, let1, let2, letb):
        newList = phrase.split()
        string =""
        for item in newList:
            if item[0] == let1 or item[0] == let2:
                string = string + item[1]
            if item[0] == letb:
                string = string + " "
        return string
        
if __name__ == '__main__':
    print decode("im like ice cream cake", "i", "c", "l")