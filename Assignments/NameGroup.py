'''
Created on Oct 12, 2017

@author: leahschwartz
'''

def calculate(names, one, two, space):
    pos = 0
    nameList = []
    correctString = ""
    answer = ""
    answerList = []
    nameList = names.split()
    while True:
        if space + 2 > len(nameList):
            break
        if space > len(nameList) - (pos + 1):
            break
        if nameList[pos] == one:
            if nameList[pos + space + 1] == two:
                answerList = nameList[pos:pos + space + 2]
                if one not in answerList[1:-1] and two not in answerList[1:-1]:
                    answer = " ".join(answerList)
                    break
                else:
                    answerList = []
        pos = pos + 1
    return answer

if __name__ == '__main__':
    print calculate("moe joe sue bo joe po fa bo sue", "joe", "bo", 2)