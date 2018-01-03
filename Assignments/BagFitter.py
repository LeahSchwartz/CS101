'''
Created on Oct 24, 2017

@author: leahschwartz
'''
def bags(strength, food):
    foodDict = {}
    answer = 0
    for group in food:
        if group not in foodDict:
            foodDict[group] = 1
        else:
            foodDict[group] += 1
    for item in foodDict:
        answer = answer + int(foodDict[item]) / strength
        if int(foodDict[item]) % strength != 0:
            answer += 1
    return answer
    
if __name__ == '__main__':
    print bags(2, ["DAIRY","DAIRY","PRODUCE","PRODUCE","PRODUCE","MEAT"])