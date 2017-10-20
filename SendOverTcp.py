import socket
import os
import time
from PyQt4 import  QtCore
class QCustomSignal(QtCore.QObject):
    sendingDataFinshed = QtCore.pyqtSignal([str])
class QTcpSender( QtCore.QThread ):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.TcpSignal = QCustomSignal()
        self.__Port = 5000
        self.__Ip   = ""
        self.__FilePath = ""
    def initSending(self , ip , port , path):
        self.__Port = port
        self.__Ip = ip
        self.__FilePath = path
    def run(self):
        SObj = socket.socket(socket.AF_INET , socket.SOCK_STREAM )
        try:
            SObj.connect((self.__Ip , self.__Port ))
            connection = SObj.makefile("wb")
            if os.path.isfile(self.__FilePath):
                with open(self.__FilePath , 'rb') as fObj :
                    fileContent  = fObj.read()
                    try:
                        connection.write('\xff\xd8')
                        connection.write(fileContent)
                        connection.write('\xff\xd9')
                        connection.flush()
                        data = SObj.recv( 1024 )
                        if ("done" in str(data)):
                            self.TcpSignal.sendingDataFinshed.emit("True")
                            print ("done sending...........")
                        else:
                            self.TcpSignal.sendingDataFinshed.emit("False")

                    except Exception as e:
                        print ("ex2" , e)
                        self.TcpSignal.sendingDataFinshed.emit("False")
        except Exception as e :
            print ("ex1" , e)
            self.TcpSignal.sendingDataFinshed.emit("False")





