'''
Created on Nov 28, 2017

@author: leahschwartz
'''
def readFile(filename):
    #returns file as list of lines
    f = open(filename)
    r = f.read()
    f.close()
    return r.split("\n")

def movieList(movieratings):
    #finds unique movies in ratings
    mSet = set() 
    for num in range(1,len(movieratings),3):
        mSet.add(movieratings[num])
    return sorted(mSet)       

def processdata(movieratings):
    movieratings = readFile(movieratings)
    ratingsDict = {}
    itemlist = movieList(movieratings)
    for num in range(0,len(movieratings),3): #builds a dict with all zeros
        if movieratings[num] not in ratingsDict:
            name = movieratings[num]
            ratingsDict[name] = [0] * len(itemlist) #num zeros == num movies
    pos = 0
    while True:
        if pos >= len(movieratings) - 3: #out of range
            break
        else:
            name = movieratings[pos]
            movie = movieratings[pos + 1]
            rating = int(movieratings[pos + 2])
            index = itemlist.index(movie) #finds movie's place in list
            ratingsDict[name][index] = rating #inserts rating in correct place
        pos += 3 #every 3 there's a new rating  
    return itemlist, ratingsDict
    
if __name__ == '__main__':
    filename = "AllMoviesRatings.txt"
    movieratings = filename
    #movieratings = readFile(filename)
    print processdata(movieratings)