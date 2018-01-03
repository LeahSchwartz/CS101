'''
Created on Oct 25, 2017

@author: leahschwartz
'''
import csv
def movieCountry(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    newDict = {}
    header = freader.next()
    for row in freader:
        country = row[3]
        if country not in newDict:
            newDict[country] = 1
        else:
            newDict[country] += 1
    info = newDict.items()
    tosortinfo = [(t[1], t[0]) for t in info]
    sortedInfo = sorted(tosortinfo)
    return sortedInfo[-10:]

def movieLength(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    newDict = {}
    header = freader.next()
    for row in freader:
        length = row[4]
        if length not in newDict:
            newDict[length] = 1
        else:
            newDict[length] += 1
    info = newDict.items()
    tosortinfo = [(t[1], t[0]) for t in info]
    sortedInfo = sorted(tosortinfo)
    return sortedInfo[-10:]
    
def movieYear(name):
    csvf = open(name,'rb')
    freader = csv.reader(csvf,delimiter=',',quotechar='"')
    newDict = {}
    header = freader.next()
    for row in freader:
        decade = row[1][2]
        if decade not in newDict:
            newDict[decade] = 1
        else:
            newDict[decade] += 1
    info = newDict.items()
    tosortinfo = [(t[1], t[0]) for t in info]
    sortedInfo = sorted(tosortinfo)
    return sortedInfo[-1][0]    
    
if __name__ == '__main__':
    print movieCountry("9600movies.csv")
    print movieLength("9600movies.csv")
    print movieYear("9600movies.csv")