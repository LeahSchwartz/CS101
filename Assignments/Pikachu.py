'''
Created on Oct 12, 2017

@author: leahschwartz
'''
def check(word):
    pos = 0
    while True:
        if len(word) == 1:
            canSay = "NO"
            break
        if pos + 1 > len(word):
            canSay = "YES"
            break
        if word[pos:pos + 2] == "pi":
            pos = pos + 2
        elif word[pos:pos + 2] == "ka":
                pos = pos + 2
        elif word[pos:pos + 3] == "chu":
                    pos = pos + 3
        else:
            canSay = "NO"
            break 
    return canSay   
    
if __name__ == '__main__':
    print check("pp")