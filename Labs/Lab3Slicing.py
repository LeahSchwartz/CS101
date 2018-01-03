'''
Created on Sep 13, 2017

@author: leahschwartz
'''
a = "computational thinking"
b = "duke university"
c = "python code"

phrase = "Do Re Me Fa So La Ti Do"
phraseList = phrase.split()    
# note that  phraseList is equal to ['Do', 'Re', 'Me', 'Fa', 'So', 'La', 'Ti', 'Do']
answer = ""
for word in phraseList:
    if word[1] != 'a':
        answer = answer + word
    print answer
if __name__ == '__main__':
    pass