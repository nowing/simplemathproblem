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
        t = (str(a) + " + " + str(b), a*b )
    elif calcType == "minus":
        t = (str(a+b) + " - " + str(b), a)
    elif calcType == "multiple":
        t = (str(a) + " × " + str(b), a*b )
    elif calcType == "divide":
        t = (str(a*b) + " ÷ " + str(b), a)
    return t

lines=[]
for i in range(10):
    lines.append(getStep("add", 3, 3)[0] + " = ");
for i in range(10):
    lines.append(getStep("minus", 3, 3)[0] + " = ");
for i in range(10):
    lines.append(getStep("multiple", 3, 2)[0] + " = ")
for i in range(10):
    lines.append(getStep("divide", 2, 2)[0] + " = ")
    
    
filename= datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".txt" 
with open("/"+filename, "w") as f:
    for line in lines:
        f.write(line + "\n")
        print(line)