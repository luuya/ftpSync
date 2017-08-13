#-*- coding:uft-8 -*-

import os
import time
import subprocess
import getFileName

class cleanFile:
    def __init__(self,file_url):
        self.file_url = file_url


        #类执行是检查文件是否存在
        if os.path.isfile(file_url):# 检验目录是否有误
            print ("File exists!")
        else:
            print ("File not exist.")
            time.sleep(5)
            exit()

    def clean(self):
        subprocess.call("cd",)
        subprocess.call(["dir",self.file_url])
        subprocess.call(["echo"," ",getFileName.GetFileName])


if __name__=="__main__":
    clean = cleanFile("D:/pipei")
    clean.clean()
