'''
Created on Dec 1, 2017

@author: leahschwartz
'''
from RecommenderForAll import averages
from RecommenderForAll import similarities
from RecommenderForAll import recommended
from ProcessAllMovies import processdata

if __name__ == '__main__':
    movieFile = "AllMoviesRatings.txt"
    movieNames, movieDict = processdata(movieFile)
    movieAverages = averages(movieNames, movieDict)
    n = 50
    keyList = ["student1367","student1008","student1256"]
    print "Movies and their average ratings"
    print "----------------------------------------"
    for item in movieAverages[:30]:
        print item[0],item[1]
    print 
    for key in keyList:
        simList = similarities(key, movieDict)
        recommendList = recommended(simList, movieNames, movieDict, n)
        print "Ratings similar to",key
        print "-------------------------"
        for item in simList[:30]:
            print item[0], item[1]
        print
        print "Recommendations for",key,"with",n,"most similar raters"
        print "-------------------------------------------------------"
        for item in recommendList[:20]:
            print item[0], item[1]
        print
        