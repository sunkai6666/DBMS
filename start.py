import os
import sys
import pandas as pa
import openpyxl

def start(path,name):
    global i
    basename=openpyxl.load_workbook(path+'/base/'+"basename.xlsx")
    bname=basename.active
    i=None
    if (not os.path.exists(path+'/base')):
        os.mkdir(path+'/base/')
    if (not os.path.exists(path+'/base/'+name)):
        os.mkdir(path+'/base/'+name)
        list=[name]
        bname.append(list)
        basename.save(path+'/base/'+"basename.xlsx")
        basename.close()