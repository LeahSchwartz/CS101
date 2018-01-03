'''
Created on Oct 31, 2017

@author: leahschwartz
'''
def makeSets(noZoo, zoos):
    bigSet = set()
    for zoo in zoos:
        if zoo != noZoo:
            zooList = zoo.split()
            zooSet = set(zooList)
            bigSet = bigSet | zooSet
    noZoo = noZoo.split()
    noZoo = set(noZoo)
    difference = noZoo - bigSet
    return difference


def numberUnique(zoos):
    answerList = []
    for element in zoos:
        unique = makeSets(element, zoos)
        if unique != set():
            answerList.append(unique)
    return len(answerList)
         
    
    
    
    
if __name__ == '__main__':
    #print makeSets("zebra bear fox elephant cat",["zebra bear fox elephant cat", "bear crocodile fox", "rhino elephant crocodile kangaroo", "elephant bear"])
    print numberUnique(["zebra bear fox elephant cat", "bear crocodile fox", "rhino elephant crocodile kangaroo", "elephant bear"])