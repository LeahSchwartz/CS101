'''
Created on Oct 31, 2017

@author: leahschwartz
'''
def namesForYearOneCourse(studentInfo, year):
    answerSet = set()
    for number in range(len(studentInfo)):
        if studentInfo[number] == year:
            answerSet.add(studentInfo[number - 1])
    return answerSet

def namesForYear(courses, year):
    finalAnswerSet = set()
    for line in courses:
        course = line.split(":")[0]
        studentInfo = line.split(":")[1:]
        oneCourse = namesForYearOneCourse(studentInfo, year)
        finalAnswerSet = finalAnswerSet | oneCourse
        finalAnswerSetSorted = sorted(finalAnswerSet)
    return " ".join(finalAnswerSetSorted)
        
 
            
    
if __name__ == '__main__':
    print namesForYear(["cps6:James:firstyear:Merlin:sophomore:Blake:senior:Yin:senior:Gauf:junior",
        "math31:Smith:firstyear:Maxwell:sophomore:Blake:senior:Yin:senior:Gauf:junior",
        "french2:Yin:firstyear:Gauf:sophomore:Knuth:senior:Lee:firstyear",
        "german1:Gauf:sophomore:Wesley:senior:Lee:firstyear:James:firstyear:Merlin:sophomore"], "firstyear")