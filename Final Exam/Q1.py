# Q1

def sumOfPositives(listOfLists):
    sum = 0
    for list in listOfLists:
        for num in list:
            if num > 0:
                sum += num
    return sum

print(sumOfPositives([[1,2,3], [-1,-2,-3], [-100], [1000]]))
