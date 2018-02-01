#!/usr/bin/env python3

import sys
import os
import csv

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def file_info(self):
        if len(self.args) == 6:
            config = self.args.index('-c')
            configfile = self.args[config+1]

            user = self.args.index('-d')
            userfile = self.args[user+1]

            gongzi = self.args.index('-o')
            gongzifile = self.args[gongzi+1]
            
            #print(configfile,userfile,gongzifile)
            return configfile,userfile,gongzifile
        else:
            print('Parameter Error')
            sys.exit(-1)
    
class Config(Args):
    def _read_config(self):
        config = {}
        if os.path.exists(self.file_info()[0]):
            with open(self.file_info()[0],'r') as file:
                for para in file.readlines():
                    config[para.split('=')[0].strip()] = para.split('=')[1].strip()
            #print(config)
            return config
        else:
            print(str(c_path),'+','not exists!')
            sys.exit(-2)
    
class UserData(Args):
    def _read_users_data(self):
        userdata = {}
        if os.path.exists(self.file_info()[1]):
            with open(self.file_info()[1],'r') as file:
                for para in file.readlines():
                    userdata[para.split(',')[0].strip()] = para.split(',')[1].strip()
            return userdata
        else:
            print(str(c_path),'+','not exists!')
            sys.exit(-3)
        

class IncomeTaxCalculator(Config,UserData):
    def calc_for_all_userdata(self):
        data = []
        #print(self._read_config()['JiShuL'])
        for gonghao,sqgongzi in self._read_users_data().items():
#            if float(sqgongzi) < float(self._read_config()['JiShuL']):
#                shebao = float(self._read_config()['JiShuL'])*(float(self._read_config()['YangLao'])+float(self._read_config()['YiLiao'])+float(self._read_config()['ShiYe']))+float(self._read_config()['GongJiJin'])
#            elif float(sqgongzi) > float(self._read_config()['JiShuH']):
#                shebao = float(self._read_config()['JiShuH'])*(float(self._read_config()['YangLao'])+float(self._read_config()['YiLiao'])+float(self._read_config()['ShiYe']))+float(self._read_config()['GongJiJin'])
#            else:
#                shebao = float(sqgongzi)*(float(self._read_config()['YangLao'])+float(self._read_config()['YiLiao'])+float(self._read_config()['ShiYe']))+float(self._read_config()['GongJiJin'])
            if int(sqgongzi) < 2193:
                shebao = 2193*0.165
            elif int(sqgongzi) > 16446:
                shebao = 16446*0.165
            else:
                shebao = int(sqgongzi)*0.165
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
            gongzidan = '{},{},{:.2f},{:.2f},{:.2f}'.format(gonghao,int(sqgongzi),shebao,tax,shgongzi)
            gz_list = gongzidan.split(',')
            data.append(tuple(gz_list))
        return data

    def export(self,default='csv'):
        result = self.calc_for_all_userdata()
        with open(self.file_info()[2],'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':
#    t = Args()
#    t.file_info()
#    c = Config()
#    c._read_config()
    s = IncomeTaxCalculator()
    s.export()
