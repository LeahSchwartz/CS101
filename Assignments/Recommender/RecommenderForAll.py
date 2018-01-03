'''
Created on Nov 29, 2017

@author: leahschwartz
'''
import ProcessAllFood
from ProcessAllFood import processdata

def sortInfo(dictionary):
    infoToSort = [(t[1],t[0]) for t in dictionary.items()] #puts number first
    sortedInfo = sorted(infoToSort) #sorts by number
    returnInfo = [(t[1],t[0]) for t in sortedInfo] #puts key first again 
    return returnInfo[::-1] #returns greatest to least

def averages(itemlist,dictratings):
    #returns tuple list of each item and and its average float rating
    avDict = {}
    for num in range(len(itemlist)):
        counter = 0 #reset for each item
        totalRatings = 0 #reset for each item
        for key, value in dictratings.items(): #goes through each rating list
            itemValue = dictratings[key][num] 
            totalRatings += itemValue #adds rating to running total
            if itemValue != 0: #non zero rating
                counter += 1 #adds one for each person who rated
        if counter != 0:
            average = float(totalRatings) / counter
            avDict[itemlist[num]] = average
    returnInfo = sortInfo(avDict)
    return returnInfo
 
def similarities(name, dictratings):
    #returns a list of tuples with person's name and similarity rating
    simDict = {}    
    valueList = []
    raterList = []   
    for key, value in dictratings.items():
        if key == name: #list of specified person's ratings
            valueList = dictratings[name] 
    for key, value in dictratings.items():
        if key != name: 
            sim = 0 #resets sim number for each person
            raterList = dictratings[key] 
            for num in range(len(raterList)):
                sim += (raterList[num] * valueList[num])
            simDict[key] = sim
    returnInfo = sortInfo(simDict) #sorts highest to lowest
    return returnInfo

def recommended(simlist,itemlist,dictratings,n):
    slist = simlist[:n]
    wDict = {}
    for item in slist:
        for key, value in dictratings.items():
            if key == item[0]:
                wDict[key] = [(float(rating) * item[1]) for rating in value]
    recommendedList = averages(itemlist, wDict) #returns average for each rest using weighted ratings
    return recommendedList
  
  
if __name__ == '__main__':
    filename = "AllFoodRatings.txt"
    itemlist = processdata(filename)[0]
    dictratings = processdata(filename)[1]
    print averages(itemlist,dictratings)
    print "simlist", similarities("Sung-Hoon", dictratings)
    simlist = similarities("Sung-Hoon", dictratings)
    n = 3
    print recommended(simlist, itemlist, dictratings, n)