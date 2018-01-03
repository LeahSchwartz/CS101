'''
Created on Oct 31, 2017

@author: leahschwartz
'''
def reversecomp(dna):
    DNAdict = {'a':'t','t':'a','c':'g','g':'c'}
    newDNA = ""
    for ch in dna:
        newDNA += DNAdict[ch]
    newDNA = newDNA[::-1]
    return newDNA
    
    
if __name__ == '__main__':
    print reversecomp("aaggtc")