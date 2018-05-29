# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import random
import datetime
from decimal import Decimal
from decimal import getcontext

def getStep(calcType, len1=1, len2=1, divideType = 'ZC'):
    # divideType: ZC=整除   YS=余数   XS=小数
    a = random.randint(10**(len1-1), 10**len1)
    b = random.randint(10**(len2-1), 10**len2)
    c = 0
    if calcType == "add":
        scale = 10**random.randint(1,2)
        scale2 = 10**random.randint(1,2)
        a = Decimal(a) / Decimal(scale)
        b = Decimal(b) / Decimal(scale2)
        t = (str(a) + " + " + str(b), str(Decimal(a) + Decimal(b)) )
    elif calcType == "minus":
        scale = 10**random.randint(1,2)
        scale2 = 10**random.randint(1,2)
        a = Decimal(a) / Decimal(scale)
        b = Decimal(b) / Decimal(scale2)
        t = (str(Decimal(a) + Decimal(b)) + " - " + str(b), str(a))
    elif calcType == "multiple":
        scale = 10**random.randint(1,2)
        scale2 = 10**random.randint(1,2)
        a = Decimal(a) / Decimal(scale)
        b = Decimal(b) / Decimal(scale2)

        t = (str(a) + " × " + str(b), Decimal(a)*Decimal(b) )
    elif calcType == "divide":
        if divideType == 'YS':
            c = random.randint(0, b)
                 
        if divideType == 'YS':
            t = (str(a*b+c) + " ÷ " + str(b), str(a) + "..." + str(c))
        elif divideType == 'ZC':
            t = (str(a*b) + " ÷ " + str(b), str(a))
        else : # XS
            scale = 10**random.randint(1,2)
            scale2 = 10**random.randint(0,1)
            scale_t = scale * scale2
            t = (str(Decimal(a)*Decimal(b)/Decimal(scale_t)) + " ÷ " + str(Decimal(b)/Decimal(scale2)), str(Decimal(a)/Decimal(scale)))
    return t

def createOneDay():
    lines=[]
    answer=[]
    
    answer.append("加:")
    for i in range(5):
        one = getStep("add", 3, 3)
        lines.append(one[0] + " = ")
        answer.append(one[1])
    
    answer.append("减:")
    for i in range(5):
        one = getStep("minus", 3, 3)
        lines.append(one[0] + " = ");
        answer.append(one[1])
    
    answer.append("乘:")
    for i in range(5):
        one = getStep("multiple", 3, 2)
        lines.append(one[0] + " = ")
        answer.append(one[1])
    
    answer.append("除:")
    for i in range(5):
        divideE = 'ZC'
        #if random.randint(1,10) <= 5:   #一半不能整除 
        divideE = 'XS'
        one = getStep("divide", 2, 2, divideE)
        lines.append(one[0] + " = ")
        answer.append(one[1])
        
    return (lines, answer)
    
    
filename= "c:\\temp\\" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".txt" 
with open(filename, "w") as f:
    dayanswer = []
    for day in range(10):
        f.write("Day " + str(day + 1) + " : " +"\n\n")
        oneday = createOneDay()
        i = 0
        for line in oneday[0]:
            f.write(line)
            i = i + 1
            if i % 2 == 0:
                f.write("\n\n")
            else:
                f.write("\t\t\t\t\t\t\t\t")
        #f.write("\n\n")
        
        daya = "Day " + str(day + 1) + " : "
        for word in oneday[1]:
            daya = daya + str(word) + "  "
        dayanswer.append(daya)

    for word in dayanswer:
        f.write(str(word) + "  " + "\n\n")

with open(filename, "r") as f:
    line = f.readlines()
    print(line)
