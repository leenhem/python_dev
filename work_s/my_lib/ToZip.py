'''
Created on 2016-12-12

@author: leenhem
'''

import zipfile

class FileToZip(object):
    def Tozip(self,filelist,zipfilename):
        zfile = zipfile.ZipFile(zipfilename, mode='w') #create zip file
        Tsum=0
        for file_list_index in range(0,len(filelist)):  #loop reportfilelist
            zfile.write(filelist[file_list_index])  #Press the file to the zip file
            Tsum=Tsum+1
        zfile.close() #After compression is completed, close the open zip file
        return Tsum