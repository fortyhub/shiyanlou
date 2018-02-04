#!/usr/bin/env python3

import sys,os,csv
import datetime,getopt,configparser
from multiprocessing import Process,Queue

queue1 = Queue()
queue2 = Queue()

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def file_info(self):
        try:
            options,args = getopt.getopt(self.args,"hC:c:d:o:",["help"])
        except getopt.GetoptError:
            sys.exit()
        cityname = 'DEFAULT'
        for name,value in options:
            if name in ("-h","--help"):
                print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata
")
            if name in ("-C"):
                cityname = value
            if name in ("-c"):
                configf = value
            if name in ("-d"):
                userfile = value
            if name in ("-o"):
                gongzifile = value
        return configf,userfile,gongzifile,cityname

class UserDate(Args):
    def get_data():    
        userdata = {}
        if os.path.exists(self.file_info()[1]):
            with open(self.file_info()[1],'r') as file:
                for para in file.readlines():
                    userdata[para.split(',')[0].strip()] = para.split(',')[1].strip()
            queue1.put(userdata)
        else:
            print(str(c_path),'+','not exists!')
            sys.exit(-3)
        

class IncomeTaxCalculator(Config,UserData):
    def calc_for_all_userdata(self):
        data = []
        for gonghao,sqgongzi in queue1.get().items():
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
        queue2.put(data)

    def export(self,default='csv'):
        result = queue2.get()
        with open(self.file_info()[2],'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':
#    t = Args()
#    t.file_info()
#    c = Config()
#    c._read_config()
    s = IncomeTaxCalculator()
    Process(target=s._read_users_data).start()
    Process(target=s.calc_for_all_userdata).start()
    Process(target=s.export).start()
