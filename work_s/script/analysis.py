'''
Created on 2016-12-8

@author: leenhem
'''
#coding:utf-8

import time
import my_lib


lasttime=time.strftime("%Y%m%d%H%M",time.localtime(time.time()-60))  #取上一分钟的日志所用的时间

#path='/var/log/tomcat_migu/'
#file='/var/log/tomcat_migu/'+lasttime+'.log'
file='C:\\Users\\leenhem\\Desktop\\test\\PresentationUploadInfo-0d8b64ac6d564815bd73c6adbe127e2e-201611300952.log'
reportfilezip_file='a.zip'

#for dirpath,dirnames,filenames in os.walk(path):
#    for filename in filenames:
#        file=os.path.join(dirpath,filename)
#===============================================================================
if __name__ == "__main__":
    analog=my_lib.AnalysisLog.AnaLog()
    reportfile_list=analog.Analog(file)
    tozip=my_lib.ToZip.FileToZip()
    report_sum=tozip.Tozip(reportfile_list, reportfilezip_file)#将zip文件名和reportfilelist传给 Tozip
    print report_sum
