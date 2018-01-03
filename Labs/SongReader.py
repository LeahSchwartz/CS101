'''
Date: October 25-26, 2017

@author: Leah Schwartz
'''

import csv

def readandprocess(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    datasg = {}
    header = freader.next()
    print "header row labels",header
    for row in freader:
        #print row
        artist = row[2]
        song = row[1]
        if artist == "Beatles":
            print "Beatles title: ",row[1]
        if artist not in datasg: 
            datasg[artist] = [song]
        else:
            datasg[artist].append(song)
    info = datasg.items() 
    tosort = [(len(t[1]),t[0]) for t in info] 
    info = sorted(tosort) 
    print info[-30:] 
        
def popularWord(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    newDict = {}
    header = freader.next()
    for row in freader:
        song = row[1].split()
        songset = set(song)
        for word in songset:
            if len(word) > 4:
                if word not in newDict:
                    newDict[word] = 1
                else:
                    newDict[word] += 1
    info = newDict.items()
    tosortinfo = [(t[1], t[0]) for t in info]
    sortedInfo = sorted(tosortinfo)
    return sortedInfo[-10:]
        
        
    
    
    

if __name__ == '__main__':
    readandprocess("top1000.csv")
    print popularWord("top1000.csv")
    
