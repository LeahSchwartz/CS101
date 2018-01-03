'''
Created on Oct 26, 2017

@author: leahschwartz
'''
import urllib2


def fileToList(url):
    #function reads in info and formats each line into list with elements needed for later
    flightInfoList = []
    source = urllib2.urlopen(url)
    for line in source:
        line = line.strip()
        flightInfo = line.split("$") #splits into elements 
        code = flightInfo[0]
        month = flightInfo[1]
        cancelledFlights = flightInfo[3]
        totalFlights = flightInfo[6]
        ontimeFlights = flightInfo[7]
        flightInfoList.append([code, month, int(cancelledFlights), int(totalFlights), int(ontimeFlights)]) #only includes needed elements
    return flightInfoList
   
    
def mostCancelled(infoList):
    #function finds airport with most months with cancellations 100 or more and how many months
    cancelledDict = {} #empty dict
    for item in infoList: 
        if item[2] >= 100: #builds dict 
            if item[0] not in cancelledDict:
                cancelledDict[item[0]] = 1
            else:
                cancelledDict[item[0]] += 1
    cancelInfo = cancelledDict.items()  
    toSortCancelInfo = [(t[1], t[0]) for t in cancelInfo] #formats with number of months first 
    sortedCancelInfo = sorted(toSortCancelInfo) #greatest num of months is last      
    numberCancelFlights = str(sortedCancelInfo[-1][0])
    cancelAirport = sortedCancelInfo[-1][1]
    return (numberCancelFlights, cancelAirport)

def busiestMonth(code, infoList):
    #returns busiest month and average flights for one airport
    busyMonthDict = {}
    for item in infoList:
        if item[0] == code:
            if item[1] not in busyMonthDict:
                busyMonthDict[item[1]] = [item[3]]
            else:
                busyMonthDict[item[1]] += [item[3]]
    for item in busyMonthDict:
        value = busyMonthDict.get(item)
        average = float(sum(value))/ len(value)
        busyMonthDict[item] = average
    busyInfo = busyMonthDict.items()  
    toSortBusyInfo = [(t[1], t[0]) for t in busyInfo] #formats with number of av. flights first 
    sortedBusyInfo = sorted(toSortBusyInfo) #greatest num of flight is last  
    averageFlights = str(sortedBusyInfo[-1][0])
    busiestMonth = sortedBusyInfo[-1][1]
    return (averageFlights, busiestMonth)

def uniqueAirports(infoList):
    #returns a list of all airport codes in data set
    uniqueAirportsList = []
    for line in infoList:
        uniqueAirportsList.append(line[0])
    uniqueAirportsList = list(set(uniqueAirportsList))
    return uniqueAirportsList

def punctualAirports(infoList):
    ontimeDict = {}
    totalFlightDict = {}
    answerList = []
    for item in infoList:
    #calculates ontime flights
        if item[0] not in ontimeDict: #building dictionary of on times
            ontimeDict[item[0]] = item[4]
        else:
            ontimeDict[item[0]] += item[4]
    for item in infoList:
    #calculates total flights
        if item[0] not in totalFlightDict: #building dictionary of totals
            totalFlightDict[item[0]] = item[3]
        else:
            totalFlightDict[item[0]] += item[3]
    for item in ontimeDict:
        ontimeDict[item] = float(ontimeDict[item]) / totalFlightDict[item] #calculating percent on time
    for key, value in ontimeDict.items():
        if value < 0.8: #taking out lower values
            ontimeDict.pop(key)
    punctualInfo = ontimeDict.items() #creating list then sorting by code
    sortedPunctualInfo = sorted(punctualInfo)
    sortedPunctualInfo = [((t[0]), str(t[1])) for t in sortedPunctualInfo]
    return sortedPunctualInfo 

if __name__ == '__main__':
    flightInfoList = fileToList("http://www.cs.duke.edu/courses/fall17/compsci101/data/airportDataOct2017.txt")
    print "Information about major airports in the United States"
    print
    print "The airport with the most months with 100 or more cancellations is", mostCancelled(flightInfoList)[1], "\n""It had", mostCancelled(flightInfoList)[0], "months with 100 or more cancellations"
    print
    print "Busiest month for each airport:"
    for airport in uniqueAirports(flightInfoList):
        print "The busiest month for", airport, "is", busiestMonth(airport, flightInfoList)[1], "with", busiestMonth(airport, flightInfoList)[0], "average flights"
    print 
    print "Airports that have >= 80% of flights on time:"
    for item in punctualAirports(flightInfoList):
        print " ".join(item)
       
    
    
    #for airport in uniqueAirports(flightInfoList):
        #print busiestMonth(airport, flightInfoList)
