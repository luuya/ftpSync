#-*- coding:utf-8 -*-

import os
import re
import time

class GetFileName:

    def __init__(self,file_url):
        self.file_url = file_url

        #调用本类时检测传入目录是否纯在
        if os.path.isdir(file_url):# 检验目录是否有误
            print ("Directory exists!")
        else:
            print ("Directory not exist.")
            time.sleep(5)
            exit()


    def getFileUrl(self):
        filelist = os.listdir(self.file_url)
        pattern = re.compile(r'gpdb_\d{4}-\d{2}-\d{2}_\d{6}\.csv') #正则匹配条件
        filelists = []
        for filename in filelist:
            search = pattern.search(filename) #正则查找的目标
            if search:
                # 使用Search获得分组信息
                filelists.append(search.group())
        return filelists





if __name__ =='__main__':
    gfn = GetFileName('D:/pipei')
    gfn.getFileUrl()