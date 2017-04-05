# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import datetime


def getStep(calcType, len1=1, len2=1):
    a = random.randint(10**(len1-1), 10**len1)
    b = random.randint(10**(len2-1), 10**len2)
    if calcType == "add":
        t = (str(a) + " + " + str(b), a+b )
    elif calcType == "minus":
        t = (str(a+b) + " - " + str(b), a)
    elif calcType == "multiple":
        t = (str(a) + " × " + str(b), a*b )
    elif calcType == "divide":
        t = (str(a*b) + " ÷ " + str(b), a)
    return t

def createOneDay():
    lines=[]
    answer=[]
    
    answer.append("加:")
    for i in range(10):
        one = getStep("add", 3, 3)
        lines.append(one[0] + " = ")
        answer.append(one[1])
    
    answer.append("减:")
    for i in range(10):
        one = getStep("minus", 3, 3)
        lines.append(one[0] + " = ");
        answer.append(one[1])
    
    answer.append("乘:")
    for i in range(10):
        one = getStep("multiple", 3, 2)
        lines.append(one[0] + " = ")
        answer.append(one[1])
    
    answer.append("除:")
    for i in range(10):
        one = getStep("divide", 2, 2)
        lines.append(one[0] + " = ")
        answer.append(one[1])
        
    return (lines, answer)
    
    
filename= datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".txt" 
with open("/"+filename, "w") as f:
    dayanswer = []
    for day in range(5):
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
        f.write("\n\n")
        
        daya = ""
        for word in oneday[1]:
            daya = daya + str(word) + "  "
        dayanswer.append(daya)

    for word in dayanswer:
        f.write(str(word) + "  " + "\n\n\n")
