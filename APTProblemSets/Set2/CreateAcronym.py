'''
Created on Sep 12, 2017

@author: leahschwartz
'''

#def acronym(phrase):
    #answer = ""
    #words = phrase.split()
    #for w in words:
        #answer = answer + w[0]
    #return answer
    
def acronym(phrase): 
    phrase = phrase.split()
    if len(phrase) == 0:
        return ""
    else:
        return phrase[0][0] + acronym(" ".join(phrase[1:]))
                 
    
if __name__ == '__main__':
    print acronym("Leah Schwartz")
