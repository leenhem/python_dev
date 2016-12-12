'''
Created on 2016-12-8

@author: leenhem
'''
import redis
import os
def connectredis(host,port,db):
    if host is None or host == '' or host == 'localhost':
        host='127.0.0.1'
        if port is None:
            port=6379
            if db is None:
                db=0
                rdb=redis.Redis(host,port,db=0)
                return rdb


if __name__=="__main__":
    f=open("lihe.txt",'r')
    r=connectredis('',6379,0)
    while True:
        lines = f.readlines(100000)
        if not lines:
            break
        for num in range(0,len(lines)):
            line=lines[num].split(',')
            key=line[0]
            value=line[1]
            r.set(key,value)
            #r.get('foo')
            print r.dbsize()
