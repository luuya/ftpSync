# -*- coding: utf-8 -*-
import os
import zipfile

#文件压缩
import zipfile
def run_zip():
    f = zipfile.ZipFile('zipfile.zip', 'w' ,zipfile.ZIP_DEFLATED)
    for filename in getFileName():
        f.write(filename)
    f.close()
#    f.zipfile.ZipFile('filename')
#    f.extractall()
#    f.close()

def getFileName():
    path = 'D:/ftpdown'
    for root, dirs, files in os.walk(path):
        return files

if __name__ == '__main__':
    #print(getFileName())
    run_zip()

    