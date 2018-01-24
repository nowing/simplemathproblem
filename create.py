# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import random
import datetime
from decimal import Decimal
from decimal import getcontext


class AddCreator(object):
    pass

class MinusCreator(object):
    pass

class MultipleCreator(object):
    pass

class DivideCreator(object):
    pass




def getStep(calcType, len1=1, len2=1, divideExactly = False, withPoint = 0):
    if withPoint == 0:
        a = random.randint(10**(len1-1), 10**len1)
        b = random.randint(10**(len2-1), 10**len2)
    else:
        a = round(random.randint(10**(len1-1+withPoint), 10**(len1+withPoint)) / (10**withPoint), withPoint)
        b = round(random.randint(10**(len2-1+withPoint), 10**(len2+withPoint)) / (10**withPoint), withPoint)
        
    if calcType == "add":
        t = (str(a) + " + " + str(b), Decimal(str(a)) + Decimal(str(b)))
    elif calcType == "minus":
        t = (str((Decimal(str(a)) + Decimal(str(b)))) + " - " + str(b), str(a))
    elif calcType == "multiple":
        t = (str(a) + " × " + str(b), Decimal(str(a)) * Decimal(str(b)) )
    elif calcType == "divide":
        if divideExactly == False:
            c = random.randint(0, b)
        else:
            c = 0
        if divideExactly == False:
            t = (str(a*b+c) + " ÷ " + str(b), str(a) + "..." + str(c))
        else:
            t = (str(a*b) + " ÷ " + str(b), str(a))
    return t

def createOneDay(perday=10):
    lines=[]
    answer=[]
    
    answer.append("加:")
    for i in range(perday):
        one = getStep("add", 3, 3, False, 1)
        lines.append(one[0] + " = ")
        answer.append(one[1])
    
    answer.append("减:")
    for i in range(perday):
        one = getStep("minus", 3, 3, False, 1)
        lines.append(one[0] + " = ");
        answer.append(one[1])
    
    answer.append("乘:")
    for i in range(perday):
        one = getStep("multiple", 3, 2, False, 1)
        lines.append(one[0] + " = ")
        answer.append(one[1])
    
    answer.append("除:")
    for i in range(perday):
        divideE = False
        if random.randint(1,10) <= 5:   #一半不能整除 
            divideE = True
        one = getStep("divide", 2, 2, divideE)
        lines.append(one[0] + " = ")
        answer.append(one[1])
        
    return (lines, answer)
    
    
filename= datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".txt" 
with open("d:/"+filename, "w") as f:
    dayanswer = []
    days = 10
    for day in range(days):
        f.write("Day " + str(day + 1) + " : " +"\n\n")
        oneday = createOneDay(5)
        i = 0
        for line in oneday[0]:
            f.write(line)
            i = i + 1
            if i % 2 == 0:
                f.write("\n\n")
            else:
                f.write("\t\t\t\t\t\t\t\t")
        f.write("\n")
        
        daya = "Day " + str(day + 1) + " : "
        for word in oneday[1]:
            daya = daya + str(word) + "  "
        dayanswer.append(daya)

    for word in dayanswer:
        f.write(str(word) + "  " + "\n\n")

with open("d:/"+filename, "r") as f:
    line = f.readlines()
    print(line)
