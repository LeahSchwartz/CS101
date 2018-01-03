'''
Dec 3, 2017

@author: ola, modified by rodger
'''
import re

def getmatches(pattern,words):
    ret = []
    for w in words:
        try:
            m = re.search(pattern,w)
            if m:
                ret.append(w)
        except:
            print 'malformed pattern:',pattern
            break
    return ret
   
def loopmatch(words):
    while True:
        pattern = raw_input('enter pattern> ')
        if len(pattern) == 0:
            break
        matches = getmatches(pattern,words)
        for m in matches:
            print m
        print "# matches:",len(matches), 'for pattern:',pattern
            

if __name__ == '__main__':
    words = []
    print "do you want to open words.txt (w) or book file (b)?"
    mode = raw_input("w or b?: ")
    
    if mode == "w":
        f = open("words.txt")
        words = [line.strip() for line in f]
    else:
        f = open("littlebrother.txt")
        words = f.read().split()
        
    loopmatch(words)
    
