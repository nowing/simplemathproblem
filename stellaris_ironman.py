# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:49:26 2018

@author: qzy
"""

import os
import time


savepath = "C:\\Users\\qzy\\Documents\\Paradox Interactive\\Stellaris\\save games"
saveid = "_-496850277"
ironman = "ironman.sav"
filename = os.path.join(savepath, saveid, ironman)

backuppath = "C:\\Users\\qzy\\Documents\\stellaris_save"

oldTime = 0
maxfile = 20

def checkNewSave():
    if os.path.exists(filename) == False:
        return False
    
    global oldTime
    timestamp = os.path.getmtime(filename)
    if timestamp != oldTime:
        oldTime = timestamp
        return True

def backupSave():
    list = os.listdir(backuppath) 
    maxidx = 0
    for i in range(0, len(list)):
        path = os.path.join(backuppath,list[i]) 
        if os.path.isfile(path):  
            name = list[i].split('.')[0]
            idx = name.split('_')[1]
            idx = int(idx)
            if idx > maxidx:
                maxidx = idx
    
    idx = maxidx + 1
    backname = "ironman_" + str(idx) + ".sav"
    fullbackname = os.path.join(backuppath, backname)
    
    if not os.path.exists(backuppath):
        os.makedirs(backuppath)
        
    open(fullbackname, "wb").write(open(filename, "rb").read())
    print(fullbackname + " created.")
    return

    
def delBackfile():
    list = os.listdir(backuppath) 
    filenum = len(list)
    if filenum <= maxfile:
        return
    
    listidx = []
    for i in range(0, len(list)):
        path = os.path.join(backuppath,list[i]) 
        if os.path.isfile(path):  
            name = list[i].split('.')[0]
            idx = name.split('_')[1]
            listidx.append(int(idx))
            
    listidx.sort()
    
    for i in range(0, filenum - maxfile):
        delidx = listidx[i]
        delname = "ironman_" + str(delidx) + ".sav"
        fulldelname = os.path.join(backuppath, delname)
        os.remove(fulldelname)
        print(fulldelname + " removed.")
    
def task():
    if checkNewSave():
        backupSave()
        delBackfile()
    return

while True:
    time.sleep(5)
    task()