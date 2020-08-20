#coding=utf-8
import configparser

class ReadIni:
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path='D:/shenjing/vsCodeWorkplace/appiumDemo/config/LocalElement.ini'
        else:
            self.file_path=file_path
        self.data=self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini
    
    #通过key获取对应的value
    def get_value(self,key):
        return self.data.get('login_element',key)
    
if __name__=='__main__':
    read_ini=ReadIni()
    print(read_ini.get_value('password'))
    

