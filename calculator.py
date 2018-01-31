#!/usr/bin/env python3

import sys
import os
import csv

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
        self.filelist = self.file_info()
    def file_info(self):
        filelist = []
        if len(self.args) == 6:
            config = self.args.index('-c')
            filelist.append(self.args[config+1])

            user = self.args.index('-d')
            filelist.append(self.args[config+1])

            gongzi = self.args.index('-o')
            filelist.append(self.args[config+1])
            
            return filelist
        else:
            print('Parameter Error')
            sys.exit(-1)
    
class Config(object):
    def __init__(self):
        self.config = self.read_config()

    def read_config(self,c_path):
        config = {}
        if os.path.exists(c_path):
            with open('c_path','r') as file:
                for para in readlines(file):
                    config[para.split('=')[0].strip()] = para.split('=')[1].strip()
            return config
        else:
            print(str(c_path),'+','not exists!')
            sys.exit(-2)
    
class UserData(object):
    def __init__(self):
        self.userdata = self.read_users_data()

    def read_users_data(self,u_path):
        userdata = {}
        if os.path.exists(u_path):
            with open('u_path','r') as file:
                for para in readlines(file):
                    userdata[para.split(',')[0].strip()] = para.split(',')[1].strip()
            return userdata
        else:
            print(str(c_path),'+','not exists!')
            sys.exit(-3)
        

class IncomeTaxCalculator(object):
    def calc_for_all_userdata(self,udata,cfg):
        data = []
        for gonghao,sqgongzi in udata.items():
            if int(sqgongzi) < int(cfg[JiShuL]):
                shebao = int(cfg[JiShuL])*(int(cfg[Yanglao])+int(cfg[YiLiao])+int(cfg[ShiYe]))+int(cfg[GongJiJin])
            elif int(sqgongzi) > int(cfg[JiShuH]):
                shebao = int(cfg[JiShuH])*(int(cfg[Yanglao])+int(cfg[YiLiao])+int(cfg[ShiYe]))+int(cfg[GongJiJin])
            else:
                shebao = int(sqgongzi)*(int(cfg[Yanglao])+int(cfg[YiLiao])+int(cfg[ShiYe]))+int(cfg[GongJiJin])
            if int(sqgongzi) <= 3500:
                tax = 0
            elif int(sqgongzi) > 3500 and int(sqgongzi) <= 5000:
                tax = (int(sqgongzi)-shebao-3500)*0.03-0
            elif int(sqgongzi) > 5000 and int(sqgongzi) <= 8000:
                tax = (int(sqgongzi)-shebao-3500)*0.1-105
            elif int(sqgongzi) > 8000 and int(sqgongzi) <= 12500:
                tax = (int(sqgongzi)-shebao-3500)*0.2-555
            elif int(sqgongzi) > 12500 and int(sqgongzi) <= 38500:
                tax = (int(sqgongzi)-shebao-3500)*0.25-1005
            elif int(sqgongzi) > 38500 and int(sqgongzi) <= 58500:
                tax = (int(sqgongzi)-shebao-3500)*0.3-2755
            elif int(sqgongzi) > 58500 and int(sqgongzi) <= 83500:
                tax = (int(sqgongzi)-shebao-3500)*0.35-5505
            elif int(sqgongzi) > 83500:
                tax = (int(sqgongzi)-shebao-3500)*0.45-13505
            shgongzi = int(sqgongzi)-shebao-tax
            data.append([gonghao,int(sqgongzi),shebao,tax,shgongzi])
        return data

    def export(self,o_path):
        result = self.calc_for_all_userdata()
        with open(o_path,'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':
    arg=Args()
    filelist=arg.filelist()
    conf=Config()
    config=conf.read_config(filelist[0])
    userdata=UserDate()
    udata=userdata.read_user_data(filelist[1])
    icome=IncomeTaxCalculator()
    data=calc_for_all_userdata(udata,config)
    icome.export(filelist[2])
