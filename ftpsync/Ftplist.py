# -*- coding: utf-8 -*-

from ftplib import FTP
import datetime
import os
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M',filename='download.log',filemode='a')


class FTP_NL:
    def __init__(self,ftp_server,username,password,port):
        self.ftp_server = ftp_server
        self.username = username
        self.password = password
        self.port = port
        self.deleteFile = []


    #返回可用的文件名
    def getFileList(self,remotepath):
        ftp = self.ftpConnect()
        ftp.cwd(remotepath)
        list = ftp.nlst()
        fileNameList = []
        for name in list:
            try:
                temp = name.split("_")
                date = temp[1]+"-"+temp[2]+"-"+temp[3]
                yesterday = getyesterday()
                if (date == yesterday):
                    fileNameList.append(name)
            except (IndexError),e:
                logging.debug(e)
        if(len(fileNameList)==0):
            logging.debug("没有符合条件的文件，等待下次程序启动")
            print "没有符合条件的文件，等待下次程序启动"
        return fileNameList



    #建立连接类
    def ftpConnect(self):
        ftp = FTP()
#       ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
        try:
            ftp.connect(self.ftp_server, self.port)  # 连接
            logging.debug("ftp连接成功")
            print "ftp连接成功"
        except(Exception),e:
            logging.debug(e)
            print "连接失败"
        try:
            ftp.login(self.username, self.password)  # 登录，如果匿名登录则用空串代替即可
            logging.debug( "ftp登陆成功")
            print "ftp登陆成功"
        except(Exception),e:
            logging.debug( e)
            print "登陆失败"
        return ftp

    #下载文件
    def downLoadFile(self,localpath,remotepath):
        self.remotepath = remotepath
        #本地路径，需要为目录
        self.localpath = localpath
        ftp = self.ftpConnect()
        logging.debug(ftp.getwelcome())  # 显示ftp服务器欢迎信息
        ftp.cwd(remotepath)
        bufsize = 1024  # 设置缓冲块大小
        if os.path.isdir(localpath):
            try:
                for filename in self.getFileList(remotepath):
                    fileStatus = False
                    fp = open(os.path.join(localpath,filename), 'wb')  # 以写模式在本地打开文件
                    fileStatus = ftp.retrbinary('RETR %s' %(filename), fp.write)  # 接收服务器上文件并写入本地文件
                    try:
                        fp.close()
                    except(IOError,Exception),e:
                        logging.debug(e)
                        print e
                    logging.debug("download-->"+filename)
                    print "download-->"+filename
                    #把成功的文件名添加到数组中去
                    if (fileStatus=='226 Transfer complete.'):
                        self.deleteFile.append(filename)
            except (IndexError,Exception) ,e:
                logging.debug( e)
            finally:
                ftp.quit()  # 退出ftp服务器
                logging.debug("断开与服务器连接")


    def deleteRemotepathFile(self,remotepath):
        ftp = self.ftpConnect()
        ftp.cwd(remotepath)
        try:
            for deletename in self.deleteFile:
                ftp.delete(deletename)
                logging.debug("delete-->"+deletename)
                print "delete-->"+deletename
        except(IndexError,Exception),e:
            logging.debug( e)
            logging.debug( "delete failed-->"+deletename)
        finally:
            self.deleteFile = []
            ftp.quit()  # 退出ftp服务器
            logging.debug("断开与服务器连接")

    #测试连接方法
    def testConnect(self,remotepath='/'):
        ftp = self.ftpConnect()
        ftp.cwd(remotepath)
        list = ftp.nlst()
        for name in list:
            logging.debug( name)

#返回符合条件的格式化后的时间(妈的，搞死人)
def getyesterday():
    today = datetime.date.today()
    unt_yesterday = today - datetime.timedelta(days=1)
    #转换为字符，分片处理
    unt_yesterday = str(unt_yesterday)
    (timeyear, timemon, timeday) = unt_yesterday.split("-")
    #月份去0处理
    timemon = int(timemon)
    #返回格式yyyy-mm-dd
    yesterday = str(timeyear)+'-'+str(timemon)+'-'+str(timeday)
    return yesterday




if __name__ == '__main__':
    # 测试方法
    def test():
        localpath = "D:\\ftpdown"
        remotepath = "receive/tccklclgl"
        ftp = FTP_NL('192.168.0.74', 'ftpu', 'ftp', '32121')
        ftp.downLoadFile(localpath, remotepath)
    test()