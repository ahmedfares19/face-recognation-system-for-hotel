from HotelDataBase import UsersDatabase
from validation import validation
from PyQt4 import QtCore , QtGui
import sys ,os , RecorderClass
from Trainer import QTrainer
from SendOverTcp import QTcpSender
from Hotel import Ui_MainWindow
import pygame
from threading import Thread
from HotelDataBase import ResidentDatabase

class MainClass(QtGui.QMainWindow ,Ui_MainWindow ,validation,UsersDatabase,ResidentDatabase):
    def __init__(self):
        pygame.init()
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        UsersDatabase.__init__(self)
        ResidentDatabase.__init__(self)

        self.VoiceTimer = QtCore.QTimer()
        self.VoiceTimer1 = QtCore.QTimer()
        self.VoiceTimer2= QtCore.QTimer()
        self.VoiceTimer3 = QtCore.QTimer()
        self.VoiceTimer4 = QtCore.QTimer()
        self.VoiceTimer5 = QtCore.QTimer()
        self.VoiceTimer6 = QtCore.QTimer()
        self.VoiceTimer7 = QtCore.QTimer()
        self.VoiceTimer8 = QtCore.QTimer()
        self.VoiceTimer9 = QtCore.QTimer()
        self.VoiceTimer10 = QtCore.QTimer()
        self.VoiceTimer11 = QtCore.QTimer()
        self.VoiceTimer12 = QtCore.QTimer()
        self.VoiceTimer13 = QtCore.QTimer()

        self.stackedWidget.setCurrentIndex(2)
        self.LogBtn.clicked.connect(self.login)
        self.LogOutBTN.clicked.connect(self.logout)
        self.AddBTN.clicked.connect(self.add)
        self.DispBTN.clicked.connect(self.view)
        self.EditBTN.clicked.connect(self.update)
        self.pushButton_10.clicked.connect(self.cancel)
        self.pushButton_14.clicked.connect(self.cancel)
        self.ShootBtN.clicked.connect(self.NewResident)
        self.pushButton.clicked.connect(self.VoiceAndTimer)
        self.show()



    def login(self):
        cnt = 0
        if self.NameValidation(str(self.UserNameLog.text())):
            self.UserNameLog.setStyleSheet("border:1px solid rgb(94, 242, 255);")
            cnt += 1
        else:
            self.UserNameLog.setStyleSheet("border:1px solid rgb(255, 61, 61);")

        if self.PassWordValidation(str(self.UserpassLog.text())):
            self.UserpassLog.setStyleSheet("border:1px solid rgb(94, 242, 255);")
            cnt += 1
        else:
            self.UserpassLog.setStyleSheet("border:1px solid rgb(255, 61, 61);")
        if cnt == 2:
            if self.LogIN(str(self.UserNameLog.text()), str(self.UserpassLog.text())):
                pygame.mixer.music.load("sounds/welcome.mp3")
                pygame.mixer.music.play()
                self.stackedWidget.setCurrentIndex(1)
                self.UserpassLog.setStyleSheet("")
                self.UserNameLog.setStyleSheet("")
                self.UserNameLog.clear()
                self.UserpassLog.clear()
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Login error")
                msgBox.setText("password or user name is incorrect");
                msgBox.setInformativeText("Please try again !")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);
                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Ok:
                    self.UserpassLog.setStyleSheet("")
                    self.UserNameLog.setStyleSheet("")
                    self.UserNameLog.clear()
                    self.UserpassLog.clear()

    def logout(self):
        self.stackedWidget.setCurrentIndex(0)
    def add(self):
        self.stackedWidget.setCurrentIndex(2)
    def view(self):
        pass
    def update(self):
        self.stackedWidget.setCurrentIndex(3)

    def cancel(self):
        self.stackedWidget.setCurrentIndex(1)

    def VoiceAndTimer(self):
        self.t = Thread(target=self.voice)
        self.t2 =Thread(target=self.Timer)
        self.t.start()
        self.t2.start()
    def voice(self):
        pygame.mixer.music.load("sounds/HotelVoice.mp3")
        pygame.mixer.music.play()
    def Timer(self):
        self.VoiceTimer.start(21*1000)
        self.VoiceTimer.timeout.connect(self.addBtnMarke)
    def addBtnMarke(self):
        self.AddBTN.setStyleSheet("border:1px solid red;color:rgb(85, 170, 255);")
        self.VoiceTimer.stop()
        self.VoiceTimer1.start(3 * 1000)
        self.VoiceTimer1.timeout.connect(self.addPage)
    def addPage(self):
        self.AddBTN.setStyleSheet("color:rgb(85, 170, 255)")
        self.stackedWidget.setCurrentIndex(2)
        self.VoiceTimer1.stop()
        self.VoiceTimer2.start(3 * 900)
        self.VoiceTimer2.timeout.connect(self.detailsMark)
    def detailsMark(self):
        self.groupBox.setStyleSheet("border:1px solid red;")
        self.VoiceTimer2.stop()
        self.VoiceTimer3.start(8 * 1000)
        self.VoiceTimer3.timeout.connect(self.cameraMark)
    def cameraMark(self):
        self.groupBox.setStyleSheet("")
        self.groupBox_25.setStyleSheet("border:1px solid red;")
        self.VoiceTimer3.stop()
        self.VoiceTimer4.start(8 * 1000)
        self.VoiceTimer4.timeout.connect(self.saveMark)
    def saveMark(self):
        self.groupBox_25.setStyleSheet("")
        self.pushButton_9.setStyleSheet("border:1px solid red;")
        self.VoiceTimer4.stop()
        self.VoiceTimer5.start(17* 1000)
        self.VoiceTimer5.timeout.connect(self.mainBack)
    def mainBack(self):
        self.pushButton_9.setStyleSheet("")
        self.stackedWidget.setCurrentIndex(1)
        self.VoiceTimer5.stop()
        self.VoiceTimer6.start(3* 1000)
        self.VoiceTimer6.timeout.connect(self.viewMark)
    def viewMark(self):
        self.DispBTN.setStyleSheet("border:1px solid red;color:rgb(85, 170, 255)")
        self.VoiceTimer6.stop()
        self.VoiceTimer7.start(3* 1000)
        self.VoiceTimer7.timeout.connect(self.viewpage)
    def viewpage(self):
        self.DispBTN.setStyleSheet("color:rgb(85, 170, 255)")
        self.stackedWidget.setCurrentIndex(4)
        self.VoiceTimer7.stop()
        self.VoiceTimer8.start(2*1200)
        self.VoiceTimer8.timeout.connect(self.mainup)
    def mainup(self):
        self.stackedWidget.setCurrentIndex(1)
        self.VoiceTimer8.stop()
        self.VoiceTimer9.start(1*1000)
        self.VoiceTimer9.timeout.connect(self.upbtn)
    def upbtn(self):
        self.EditBTN.setStyleSheet("border:1px solid red;color:rgb(85, 170, 255)")
        self.VoiceTimer9.stop()
        self.VoiceTimer10.start(2*1000)
        self.VoiceTimer10.timeout.connect(self.uppage)
    def uppage(self):
        self.stackedWidget.setCurrentIndex(3)
        self.EditBTN.setStyleSheet("color:rgb(85, 170, 255)")
        self.VoiceTimer10.stop()
        self.VoiceTimer11.start(4 * 1000)
        self.VoiceTimer11.timeout.connect(self.upmain)
    def upmain(self):
        self.stackedWidget.setCurrentIndex(1)
        self.VoiceTimer11.stop()
        self.VoiceTimer12.start(1 * 1000)
        self.VoiceTimer12.timeout.connect(self.log)
    def log(self):
        self.LogOutBTN.setStyleSheet("border:1px solid red;color:rgb(255, 92, 51)")
        self.VoiceTimer12.stop()
        self.VoiceTimer13.start(1 * 1000)
        self.VoiceTimer13.timeout.connect(self.mm)
    def mm(self):
        self.LogOutBTN.setStyleSheet("color:rgb(255, 92, 51)")
        self.VoiceTimer13.stop()
        self.t.daemon
        self.t2.daemon

    def NewResident(self):
        cnt =0
        if not self.NameValidation(str(self.REGNAME.text())):
            self.REGNAME.setStyleSheet("border:1px solid rgb(255, 61, 61)")
        else:
            self.REGNAME.setStyleSheet("border:1px solid rgb(94, 242, 255)" )
            cnt +=1

        if not self.NidValidation(str(self.REGNID.text())):
            self.REGNID.setStyleSheet("border:1px solid rgb(255, 61, 61)")
        else:
            self.REGNID.setStyleSheet("border:1px solid rgb(94, 242, 255)")
            cnt += 1
        if cnt == 2:
            self.InsertResident(str(self.REGNID.text()),str(self.REGNAME.text()),
                                str(self.RoomCB.currentText()) ,str(self.PersonCB.currentText())   ,
                                str(self.dateEdit.date()),str(self.timeEdit.time()),str(self.dateEdit_2.date()),
                                str(self.timeEdit_2.time()))










    def TakeNewDataSet(self):
        ClientId = str(self.REGNAME.text()).strip(" ")
        if len(ClientId):
            folderPath = os.path.join(os.getcwd(),"dataSet" , ClientId)
            self.recordObj = RecorderClass.QRecorderClass(
                self.CameraLB,
                folderPath
            )
            self.recordObj.temp.takingDataSetFinshed.connect(self.foo)
            self.recordObj.Record()

    def foo(self, filePath):
        print ("start train")
        self.stackedWidget.setCurrentIndex(2)
        self.tempTrainer = QTrainer(str(filePath))
        self.tempTrainer.TrainingSignal.TrainingFinshed.connect(self.sendFiles)
        self.tempTrainer.start()

    def sendFiles(self, outpath):
        print ("start send")
        self.tcpObj = QTcpSender()
        self.tcpObj.initSending("192.168.1.4", 5010, outpath)
        self.tcpObj.TcpSignal.sendingDataFinshed.connect(self.doneReceiveing)
        self.tcpObj.start()

    def doneReceiveing(self, event):
        self.stackedWidget.setCurrentIndex(0)


app = QtGui.QApplication(sys.argv)
m = MainClass()
app.exec_()
