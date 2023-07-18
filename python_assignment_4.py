#!/usr/bin/python
#Filename : backup.py

import shutil, os
import datetime

current_date = str(datetime.datetime.now())[:19]
current_date=current_date.replace(" ","_").replace(':','-')
print(current_date)
source_path = input('Enter source path : ')
target_path = input('Enter destination path : ')

path1 = os.path.exists(source_path)
path2 = os.path.exists(target_path)

if (path1==True and path2 == True):
    target_path=target_path+str(current_date)
    print(target_path)
    shutil.move(source_path, target_path)
else:
    print("Enter valid path")