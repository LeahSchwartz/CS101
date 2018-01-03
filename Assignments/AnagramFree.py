'''
Created on Oct 18, 2017

@author: leahschwartz
'''
def getMaximumSubset(words):
    return len(set(["".join(sorted(w)) for w in words]))
   
    
if __name__ == '__main__':
    print getMaximumSubset(["abcd","abac","aabc","bacd"])
    