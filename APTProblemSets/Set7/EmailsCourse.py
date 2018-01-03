'''
Created on Nov 7, 2017

@author: leahschwartz
'''
def emailsLargest(courses):
    courseDict = {}
    largestCourse = 0
    largestCourseEmails = []
    largestCourseName = ""
    for element in courses:
        splitElement = element.split(":")
        courseName = splitElement[0]
        email = splitElement[2]
        if courseName not in courseDict:
            courseDict[courseName] = [email]
        else:
            courseDict[courseName] += [email]
    print courseDict
    for key,value in courseDict.items():
        if len(value) > largestCourse:
            largestCourseEmails = value
            largestCourse = len(value)
            largestCourseName = key
        elif len(value) == largestCourse:
            if key < largestCourseName:
                largestCourseEmails = value
                largestCourse = len(value)
                largestCourseName = key 
    return " ".join(sorted(largestCourseEmails))

if __name__ == '__main__':
    print emailsLargest(["CompSci 100:Fred Jack Smith:fjs@duke.edu", 
  "History 117:Fred Jack Smith:fjs@duke.edu", 
  "CompSci 102:Arielle Marie Johnson:amj@duke.edu", 
  "CompSci 100:Arielle Marie Johnson:amj@duke.edu", 
  "CompSci 006:Bertha White:bw@duke.edu",
  "Econ 051:Bertha White:bw@duke.edu", 
  "English 112:Harry Potter:hp@duke.edu",
  "CompSci 100:Harry Potter:hp@duke.edu"])