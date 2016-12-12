'''
Created on 2016-12-12

@author: leenhem
'''
import logging
import time

nowtime=time.strftime("%Y%m%d%H",time.localtime(time.time())) #The time in the name of the log file to print per day
class ToLogger(object):
    def Tolog (self,logfile,message):
        log_file=logfile+str(nowtime)+'.log'
        logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename=log_file,  
                    filemode='a')
        logging.debug(message)