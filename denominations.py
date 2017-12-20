import random
from itertools import combinations


def getExactChangeNum(d):
    # d1,d2,d3,d4 is the 4 denominations from least to greatest
    changes = []
    # fill array with the amt of change itself
    for i in range(239):
        changes.append(i)
    # change array to reflect actual exact change num 
    for j in range(239):
   #     print ("coins = " + str(j + 1))
        if (j == d[0] - 1 or j == d[1] -1  or j == d[2] - 1 or j == d[3] - 1 ):
                changes[j] = 1
  #              print("exact change " + str(changes[j]))
                continue
        else:
            if (j >= d[3]):
                d1 = changes[j - d[3]] + 1
   #             print("d1 " + str(d1))
            else:
   #             print("exact change " + str(changes[j]))
                continue
            if (j >= d[2]):
                d2 = changes[j - d[2]] + 1
   #             print("d2 " + str(d2))  
            else:
                changes[j]  = d1 
   #             print("exact change " + str(changes[j]))
                continue
            if (j >= d[1]):
                d3 = changes[j - d[1]] + 1 
   #             print("d3 " + str(d3)) 
            else:
                changes[j] =  min(d1,d2) 
   #             print("exact change " + str(changes[j]))
                continue
            if (j >= d[0]):
                d4 = changes[j - d[0]] + 1
  #              print("d4 " + str(d4)) 
                changes[j] = min(d1,d2,d3,d4) 
   #             print("exact change " + str(changes[j]))
            else:
                changes[j] =  min(d1,d2,d3)
   #             print("exact change " + str(changes[j]))
    return changes

#calculates ever single possible change and sums it
def sumExactChangeNum(ch ,N): 
    sum = 0
 #   print("start")
    for num in range(239): 
        if ((num + 1)%5 == 0):
            sum += (N*ch[num])
 #           print("change =" + str(num + 1))
 #           print ("num of coins =" + str(ch[num]))
        else:
            sum += ch[num]
#            print("change =" + str(num + 1))
#            print ("num of coins =" + str(ch[num]))
    return sum
# generates denominations 
def generate(poundValue, N):
    optimalDenom = []
    optimalChange = 100000
    # max for the largest denomination
    max  = int(poundValue/2)
    # every single combination of denoms up till max
    comb = list(combinations(range(4, max, 1),3))
    for l in comb:
        # sort in reversed order
        denom = sorted(l, reverse=True)
        denom.append(1)
        # impractical for denomications to be close to each other or super big
        if (denom[1] < 50 and denom[2] < 30 and denom[0] - denom[1] > 15 and denom[1] - denom[2] > 15):
            values = getExactChangeNum(denom)
            num = sumExactChangeNum(values, N)
            if (num < optimalChange):
                print(denom)
                print("num")
                print(num)
                optimalDenom = denom     
                optimalChange = num
    print(optimalChange)
    return optimalDenom

while(True):
    n = int(input("Enter N"))
    print(sumExactChangeNum(getExactChangeNum([55,35,5,1]),n))
    print(generate(240, n))