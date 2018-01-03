'''
Created on Dec 2, 2017

@author: leahschwartz
'''
from RecommenderForAll import averages
from RecommenderForAll import similarities
from RecommenderForAll import recommended
from ProcessAllBooks import processdata

if __name__ == '__main__':
    bookTitles = "AllBooksAuthors.txt"
    bookRatings = "AllBooksRatings.txt"
    bookNames, bookDict = processdata(bookTitles,bookRatings)
    bookAverages = averages(bookNames, bookDict)
    n = 20
    keyList = ["Brix","Brian","Hideo"]
    print "Books and their average ratings"
    print "----------------------------------------"
    for item in bookAverages[:20]:
        print item[0],item[1]
    print 
    for key in keyList:
        simList = similarities(key, bookDict)
        recommendList = recommended(simList, bookNames, bookDict, n)
        print "Ratings similar to",key
        print "-------------------------"
        for item in simList[:20]:
            print item[0], item[1]
        print
        print "Recommendations for",key,"with",n,"most similar raters"
        print "-------------------------------------------------------"
        for item in recommendList[:10]:
            print item[0], item[1]
        print