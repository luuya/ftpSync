# -*- coding: utf-8 -*-
from Ftplist import FTP_NL

class START:
    def start(self):
        self.localpath = "D:\\ftpdown"      #本地下载路径
        self.remotepath = "receive/tccklclgl"   #远程工作目录
        ftp = FTP_NL('192.168.0.74', 'ftpu', 'ftp', '32121')
        ftp.downLoadFile(self.localpath,self.remotepath)
        ftp.deleteRemotepathFile(self.remotepath)

st = START()
st.start()








