'''
Created on Oct 16, 2017

@author: leahschwartz
'''
def decryptWord(library,code):
    indx = 0
    while True:
        if indx >= len(library):
            decryptedLetter = "?"
            break
        if code == library[indx][2:]:
            decryptedLetter = library[indx][0]
            break
        indx = indx + 1
    return decryptedLetter   

def decrypt(library,message):
    answer = ""
    for code in message.split():
        newLetter = decryptWord(library,code)
        answer = answer + newLetter
    return answer
    
    
    
if __name__ == '__main__':
    print decrypt(["O ---"], "... --- ...")
    