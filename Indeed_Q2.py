import sys
import os
import math

def  getMinimumUniqueSum(arr):
    return [getCountOfSquares(*nums.split()) for nums in arr]

def getCountOfSquares(lb, ub):
    return sum([isSquare(x) for x in range(int(lb), int(ub)+1)])

def isSquare(n):
    if n**(.5)==math.floor(n**(.5)):
        return 1
    return 0

if __name__ == '__main__':
    #print getCountOfSquares([1,25])

    _arr = ["3 9", "17 24"]
    res = getMinimumUniqueSum(_arr);

    print res


