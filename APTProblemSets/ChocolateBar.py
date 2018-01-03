'''
Created on Oct 31, 2017

@author: leahschwartz
'''
def uniqueLetter(letters):
    letterList = list(letters)
    letterSet = set(letters)
    if len(letterList) == len(letterSet):
        return True
    else:
        return False

def maxLength(letters):
    lengthSet = set()
    if len(set(letters)) == 1:
        return 1
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            if uniqueLetter(letters[i:j + 1]):
                lengthSet.add(len(letters[i:j + 1]))
    return sorted(lengthSet)[-1]
    
if __name__ == '__main__':
    print maxLength("aaaa")