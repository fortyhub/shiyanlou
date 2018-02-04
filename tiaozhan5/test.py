#!/usr/bin/env python3

import sys,os,csv
import datetime,getopt,configparser

try:
    options,args = getopt.getopt(sys.argv[1:],"hC:c:d:o:",["help","City=","conf=","data=","output="])
except getopt.GetoptError:
    sys.exit()
cityname = 'DEFAULT'
for name,value in options:
    if name in ("-h","--help"):
        print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata")
    if name in ("-C","--City"):
        cityname = value
    if name in ("-c","--conf"):
        configfile = value
    if name in ("-d","--data"):
        userfile = value
    if name in ("-o","--output"):
        gongzifile = value
print(cityname,configfile,userfile,gongzifile)

conf = configparser.ConfigParser()
conf.read('configfile')
sections = conf.sections()
print(sections)
yanglao=conf.getfloat('DEFAULT','JiShuH')
print(yanglao)
v = conf.items('DEFAULT')
print(v)



