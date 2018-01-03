'''
Created on Sep 14, 2017

@author: leahschwartz
'''
import urllib2
import random
from Finder.Finder_items import item

def fileToList(url):
    '''
    This function reads a file from a given url 
    returns a list of strings where each string 
    represents one line from the file
    '''
    alist = []
    source = urllib2.urlopen(url)
    magnitude = ""
    for line in source:
        items = line.strip()
        items = items.replace("%","$")
        items = items.split("$")
        magnitude = items[0]
        items[0] = items[1]
        items[1] = magnitude
        items = items[0] + ", " + items[1] + ", " + items[2]
        alist.append(items)
    return alist
       
def numberOfType(alist, someType):
    #returns number of type earthquake in list
    returnNumber = 0
    for line in alist:
        if "earthquake" in line:
            returnNumber = returnNumber + 1    
    return returnNumber

def printQuakes(alist, num):
    #prints a given number of earthquakes formated as strings from a list
    if num == -1:
        print alist
    if num >= 1 and num <= len(alist):
        for item in range(num):
            print alist[item]
    if num >= 1 and num > len(alist):
        for item in range(len(alist)):
            print alist[item]

def getParts(string):
    #breaks string into three parts: magnitude as a float, type as string, location as string
    magnitude =""
    newList = string.split(",")
    magnitude = float(newList[1])
    newList[1] = newList[0]
    newList[0] = magnitude
    if len(newList) > 3:
        newList[2] = newList[2] + "," + newList[3]
        newList.pop(3)
    return newList

def bigQuakes(decimal, thisList):
    #returns earthquakes that are a certain magnitude or greater as a list
    greaterEarthquakes = []
    newLine =[]
    for line in thisList:
        newLine = getParts(line)
        if decimal <= newLine[0]:
            greaterEarthquakes.append(newLine[1] + ", " + str(newLine[0]) + "," + newLine[2])
    return greaterEarthquakes

def locationQuakes(place, thisList):
    #returns a list of earthquakes in a given place
    placeList = []
    returnList = ""
    for line in thisList:
        line = line.split()
        lineAsString = ""
        if line[-1] == place:
            for entry in line:
                lineAsString = lineAsString + " " + entry
                lineAsString = lineAsString.strip() 
            placeList.append(lineAsString)
    return placeList
        
def printType(thisList): 
    #prints different types of events in a list 
    newList = []
    listof = []
    parts = []
    for l in thisList:
        parts = getParts(l)
        typeEq = parts[1]
        if typeEq not in listof:
            listof.append(typeEq)
    for l in listof:
        print l
    
def randomEarthquakes(alist):
    #selects random lines from a list and returns them
    random.shuffle(alist)
    return alist

def largestQuake(alist):
    #returns largest earthquake info from a list of quakes
    mag = 0
    newQuake = []
    bigQuake = []
    for l in alist:
        newQuake = getParts(l)
        if mag < newQuake[0]:
            mag = newQuake[0]
            bigQuake = l
    return bigQuake

def earthquakeInBetween(fdecimal, sdecimal, alist):
    #returns earthquakes between certain magnitudes (inclusive) 
    earthquake = []
    resultList = []
    for line in alist:
        earthquake = getParts(line)
        if earthquake[0] >= fdecimal and earthquake[0] <= sdecimal:
            resultList.append(line)          
    return resultList     
 
if __name__ == '__main__':
    urlstart = "http://www.cs.duke.edu/courses/compsci101/fall17/data/"
    datafile = "earthqDataAug14-Sep13-2017.txt"
    #datafile = "earthqDataSmallSep2017.txt"
    eqList = fileToList(urlstart+datafile)
    
    print "Information about Earthquakes from the 30 days"
    print "leading up to September 13, 2017."
    print   
    print "Number of lines in the file is:", len(eqList)
    print
    numEarthquakes = numberOfType(eqList, "earthquake")
    print "Number of lines categorized as earthquakes in the file is: ", numEarthquakes
    print
    print "First ten lines in the file:"
    printQuakes(eqList, 10)
    print
    print "First ten earthquake in Puerto Rico are:"
    print 
    printQuakes(locationQuakes("Rico", eqList),10)
    print 
    print "Number of earthquakes in Mexico is", ((len(locationQuakes("Mexico", eqList))))
    print
    print "Number of earthquakes in California that are 1.0 or greater and less than 3.0 is:" 
    print len(earthquakeInBetween(1.0, 3.0, locationQuakes("California", eqList)))
    print
    print "First five earthquakes in Alaska with magnitude 3.0 or larger:"
    printQuakes(bigQuakes(3.0, locationQuakes("Alaska", eqList)), 5)
    print 
    print "Types of activity: "
    printType(eqList)
    print
    print "Largest quake is: " 
    printQuakes(largestQuake(eqList), -1) 
    print 
    print "Largest magnitude earthquake in Hawaii is:"
    printQuakes(largestQuake(locationQuakes("Hawaii", eqList)), -1)
    print
    print "Ten random earthquakes in Peru:"
    printQuakes(randomEarthquakes(locationQuakes("Rico", eqList)), 10)
    print
    print "done processesing"

   
    
    
    