﻿'''
Created on 2016-12-12

@author: leenhem
'''
#coding:utf-8
import json
import my_lib.ToLog

class AnaLog(object):
    def Analog(self,file):
        print file
        f=open(file,'rU')
        data=f.readlines()
        for i in range(0,len(data)):
            line_arg=data[i].split('-||-')  #每条日志都是以-||- 分割的
            line_json= line_arg[len(line_arg)-1] #取出每条日志的json格式的字符
            tmp_line_json=json.loads(line_json)["deviceInfo"] #取出每条json中的deviceInfo字段
            end_line_json=json.loads(tmp_line_json)["store_path"].split(";") #取出deviceInfo字段中的store_path字段，并以；分割开
            reportfile_list=[]
            
            logfile='reporttozip_.log'
            for j in range(0,len(end_line_json)-1): #读取store_path字段中的reportfile,遍历报告文件
                reportfile_list.append(end_line_json[j]) #将每分钟的log里面的report写进一个reportfilelist
                log=my_lib.ToLog.ToLogger()
                log.Tolog(logfile,end_line_json[j])
                f.close()
                return reportfile_list
        