#!/usr/bin/python
#Filename : backup.py

import shutil, os, sys
import datetime

source = sys.argv[1]
target = sys.argv[2]

path1 = os.path.exists(source)
path2 = os.path.exists(target)

def backup(a, b):
    shutil.move(a, b)

if (path1==True and path2 == True):
    current_date = str(datetime.datetime.now())[:19]
    current_date=current_date.replace(" ","_").replace(':','-')
    target=target+current_date
    backup(source, target)
else:
    print("Enter valid path")