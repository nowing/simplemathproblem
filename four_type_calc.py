# -*- coding: utf-8 -*-
import re
import random
import datetime
from decimal import Decimal
from decimal import getcontext
import codecs

def multiply_divide(s):                               #计算一个不含括号的最小乘除单元，用split分隔*或/然后计算
    ret = Decimal(float(s.split('*')[0])) * Decimal(float(s.split('*')[1])) if '*' in s else Decimal(float(s.split('/')[0])) / Decimal(float(s.split('/')[1]))
    return ret
 
def remove_md(s):                                     # 将不含括号的表达式里的乘除先递归计算完
    if '*' not in s and '/' not in s:
        return s                                      # 没有乘除的话递归结束
    else:                                             # 匹配一个最小乘除单元，调用multiply_divide计算，将结果拼接成一个新的表达式进行递归处理
        k = re.search(r'-?[\d\.]+[*/]-?[\d\.]+', s).group()
        s = s.replace(k, '+' + str(multiply_divide(k))) if len(re.findall(r'-', k)) == 2 else s.replace(k, str(multiply_divide(k)))
        return remove_md(s)
 
def add_sub(s):                                       # 计算没有乘除的表达式，得出最后不包含括号表达式的运算结果
    l = re.findall('([\d\.]+|-|\+)', s)               # 将表达式转换成列表，
    if l[0] == '-':                                   # 如果第一个数是负数，对其进行处理
        l[0] = l[0] + l[1]
        del l[1]
    sum = float(l[0])
    for i in range(1, len(l), 2):                     # 循环计算结果
        if l[i] == '+' and l[i + 1] != '-':  # 加非负数
            sum = Decimal(sum) + Decimal(float(l[i + 1]))
            #sum += float(l[i + 1])
        elif l[i] == '+' and l[i + 1] == '-': # 加负数
            sum = Decimal(sum) - Decimal(float(l[i + 2]))
            #sum -= float(l[i + 2])
        elif l[i] == '-' and l[i + 1] == '-': # 减负数 
            sum = Decimal(sum) + Decimal(float(l[i + 2]))
            #sum += float(l[i + 2])
        elif l[i] == '-' and l[i + 1] != '-': # 减非负数
            sum = Decimal(sum) - Decimal(float(l[i + 1]))
            #sum -= float(l[i + 1])
    return sum
 
def basic_operation(s):                           # 计算一个基本的4则运算
    s = s.replace(' ', '')
    return add_sub(remove_md(s))                  # 调用前面定义的函数，先乘除，后加减
 
def calculate(expression):                        # 计算包含括号的表达式
    if not re.search(r'\([^()]+\)', expression):                    # 匹配最里面的括号，如果没有的话，直接进行运算，得出结果
        return basic_operation(expression)
    k = re.search(r'\([^()]+\)', expression).group()                # 将匹配到的括号里面的表达式交给basic_operation处理后重新拼接成字符串递归处理
    expression = expression.replace(k, str(basic_operation(k[1:len(k) - 1])))
    return calculate(expression)
 
    
#test
#s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#print('用eval计算出来的值为：{}\n计算器计算出来的值为：{}'.format(eval(s), calculate(s)))

# 生成含count个计算项的四则运算
def createExp(count = 5, hasBrackets = False):
    s = ''
    braStart = False
    braEnd = False
    hasMid = False
    for i in range(0, count):
        z = random.randint(1,3)   #整数部分
        x = random.randint(1,2)   #小数部分

        if hasBrackets and not braStart and i != count-1 and not s.endswith('/'):
            if random.randint(0, 2) == 2:
                s = s + '('
                braStart = True
        
        if s.endswith('*'):  # 乘时只算 0.1 * n 形式
            s = s + str(createDivTen() * random.randint(1, 9))
        elif s.endswith('/'): #除时只算 0.1 形式
            s = s + str(createDivTen())
        else:
            s = s + str(createNum(z, x))
            
        if braStart and not braEnd and hasMid:
            s = s + ')'
            braEnd = True
            
        if i != count-1:   # 不是最后一个数字，取得计算符
            optList = '+-*/'
            
            if braStart and not braEnd:  # 在括号内，只做加减运算
                optList = '+-'
                hasMid = True
                    
            if '*' in s:
                optList = optList.replace('*', '') 
            if '/' in s:
                optList = optList.replace('/', '')
            s = s + getRandOperator(optList)
    


    return s
        
    

# 生成一个带小数，共total位，其中小数部分xiao位
def createNum(total = 5, xiao = 3):
    num = Decimal(random.randint(10**(total-1), 10**total - 1)) / Decimal(10**xiao)
    return num

# 生成0.1格式的小鼠
def createDivTen():
    r = random.randint(1,3)
    num = 10**r
    return Decimal(1) / Decimal(num)

# 从optList中取得一个随机运算符号
def getRandOperator(optList):
    s = optList [random.randint(0, len(optList)-1)]
    return s

# 删除右边多余的0
def removeRight0(dec):
    s = str(dec)
    total = len(s)
    for i in range(1, total):
        if s.endswith('0') or s.endswith('.'):
           s = s[0:len(s) - 1]
    return s

# 一天的题目和答案
def oneDay():
    lines=[]
    answer=[]
    
    count = 5 # 每天的题目数
    for i in range(count):
        exp = createExp(random.randint(4,5), True)
        ans = removeRight0(calculate(exp))
        
        lines.append(exp)
        answer.append(ans)
        
    return (lines, answer)
  
# 生成n天的题目，并保存成文件
def createDoc():
    filename= "c:\\temp\\" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".txt" 
    getcontext().prec = 10
    with codecs.open(filename, "w", 'utf-8') as f:
        dayanswer = []
        days = 7  # 生成n天题目
        for day in range(days):
            f.write("Day " + str(day + 1) + " : " +"\n\n")
            oneday = oneDay()
            i = 1
            for line in oneday[0]:
                out = line.replace('/','÷')
                f.write(str(i) + '. ' + out)
                i = i + 1
                f.write("\n")    #题目换行
            
                for blanki in range(7):
                    f.write("\n")   #题目间留空白
            
            i = 1
            daya = "Day " + str(day + 1) + " : "
            for word in oneday[1]:
                daya = daya + str(i) + ': ' +  str(word) + "  "
                i = i + 1
            dayanswer.append(daya)
    
        for word in dayanswer:
            f.write(str(word) + "  " + "\n\n")
    
    with open(filename, "r") as f:
        line = f.readlines()
        print(line)


createDoc()