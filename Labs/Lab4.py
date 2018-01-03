'''
Created on Sep 17, 2017

@author: leahschwartz
'''


def process(name):
    f = open(name)
    answer = []
    for line in f:
        line = line.strip()
        line = line.split(";")
        answer.append(line)
    return answer          

def classAverage(data):
    runningAverage = []
    for line in data:
        line[1] = float(line[1])
        runningAverage.append(line[1])
    newAverage = sum(runningAverage) / len(runningAverage) 
    return newAverage

def maxGrade(data):
    listGrades = []
    for line in data:
        line[1] = float(line[1])
        listGrades.append(line[1])
    answer = max(listGrades)
    return answer

def howManyInRange(data, year1, year2):
    goodYearKids = []
    for line in data:
        if float(line[2]) >= year1 and float(line[2]) <= year2:
            goodYearKids.append(line)
    return len(goodYearKids)

def namesForGrades(data, grade1, grade2):
    goodGradeKids = []
    for line in data:
        if float(line[1]) >= grade1 and float(line[1]) <= grade2:
            goodGradeKids.append(line[0])
    return goodGradeKids
    
if __name__ == '__main__':
    filename ="grades.txt"
    data = process(filename)
    for each in data:
        print each
    print
    print "Average grade is ", classAverage(data)
    print "Maximum grade is ", maxGrade(data)
    grade1 = 80
    grade2 = 90
    print "Names of people with grades between ", grade1, " and ", grade2, " inclusive"
    names = namesForGrades(data, 90, 95)
    for line in names:
        print line
    # ADD CODE TO PRINT the names one per line
    print
    year1 = 1995
    year2 = 1997
    print "Number born from ",year1,"to",year2,"is",
    print howManyInRange(data, 1991, 1994)
    
