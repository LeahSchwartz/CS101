'''
Created on Dec 1, 2017

@author: leahschwartz
'''
from RecommenderForAll import averages
from RecommenderForAll import similarities
from RecommenderForAll import recommended
from ProcessAllFood import processdata

if __name__ == '__main__':
    foodFile = "AllFoodRatings.txt"
    foodItems, foodDict = processdata(foodFile)
    restAverages = averages(foodItems, foodDict)
    n = 3
    print "RESTAURANTS"
    for item in foodItems:
        print item
    print
    print "RATER and their Ratings:"
    for key,value in foodDict.items():
        print key,value
    print
    print "Restaurants and their average ratings"
    print "----------------------------------------"
    for item in restAverages:
        print item
    print 
    for key in foodDict:
        simList = similarities(key, foodDict)
        recommendList = recommended(simList, foodItems, foodDict, n)
        print "Ratings similar to",key
        print "-------------------------"
        for item in simList:
            print item[0], item[1]
        print
        print "Recommendations for",key,"with",n,"most similar raters"
        print "-------------------------------------------------------"
        for item in recommendList:
            print item
        print
        