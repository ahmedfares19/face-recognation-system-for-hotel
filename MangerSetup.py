from PyQt4 import QtGui , QtCore
from HotelDataBase import UsersDatabase
from validation import validation
import pygame
import sys

from manger import Ui_MainWindow

class Mangersetup(QtGui.QMainWindow ,UsersDatabase,Ui_MainWindow,validation):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        UsersDatabase.__init__(self)
        self.setupUi(self)
	pygame.init()
        self.stackedWidget.setCurrentIndex(0)
        self.LogBtn_2.clicked.connect(self.MangerLogin)
        self.pushButton_3.clicked.connect(self.AddPage)
        self.pushButton_2.clicked.connect(self.DelPage)
        self.pushButton.clicked.connect(self.AddAndDel)
        self.LogBtn_4.clicked.connect(self.AddAndDel)
        self.LogBtn_3.clicked.connect(self.AddUser)
        self.SignBtn_2.clicked.connect(self.DeleteUser)
        self.show()

    def MangerLogin(self):
        cnt = 0
        if self.NameValidation(str(self.UserNameLog_2.text())):
            self.UserNameLog_2.setStyleSheet("border:1px solid rgb(94, 242, 255);")
            cnt +=1

        else:
            self.UserNameLog_2.setStyleSheet("border:1px solid rgb(255, 61, 61);")


        if self.PassWordValidation(str(self.UserpassLog_2.text())):
            self.UserpassLog_2.setStyleSheet("border:1px solid rgb(94, 242, 255);")
            cnt += 1
        else:
            self.UserpassLog_2.setStyleSheet("border:1px solid rgb(255, 61, 61)")

        n , p = self.mangerValidation(self.UserNameLog_2.text(),self.UserpassLog_2.text())
        if cnt == 2:
            if not n== 1:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Login error")
                msgBox.setText(" Incorrect name");
                msgBox.setInformativeText("Please try again !")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);

                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Ok:
                    self.UserNameLog_2.setStyleSheet("border:1px solid rgb(255, 61, 61);")
            elif not p == 1:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Login error")
                msgBox.setText(" Incorrect password");
                msgBox.setInformativeText("Please try again !")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);


                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Ok:
                    self.UserpassLog_2.setStyleSheet("border:1px solid rgb(255, 61, 61)")

            else:
                pygame.mixer.music.load("sounds/welcome.mp3")
                pygame.mixer.music.play()
                self.stackedWidget.setCurrentIndex(1)
                users = self.UserNames()
                self.comboBox.addItems(users)

    def AddPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def DelPage(self):

        self.stackedWidget.setCurrentIndex(3)

    def AddAndDel(self):
        if len(str(self.UserpassLog_5.text())) > 0 or len(str(self.UserNameLog_3.text())) > 0 or len(str(self.UserpassLog_3.text())) > 0 or len(str(self.UserpassLog_4.text())) > 0:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setWindowTitle("Cancelling")
            msgBox.setText("Are you sure that you want to cancel");
            msgBox.setInformativeText("You will lose entered data")
            msgBox.setStandardButtons(QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
            msgBox.setDefaultButton(QtGui.QMessageBox.No)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save);
            ret = msgBox.exec_();
            if ret == QtGui.QMessageBox.No:
                pass
            else:
                self.stackedWidget.setCurrentIndex(1)
                self.UserpassLog_5.clear()
                self.UserNameLog_3.clear()
                self.UserpassLog_3.clear()
                self.UserpassLog_4.clear()
        else:
            self.stackedWidget.setCurrentIndex(1)
            self.UserpassLog_5.clear()
            self.UserNameLog_3.clear()
            self.UserpassLog_3.clear()
            self.UserpassLog_4.clear()

    def AddUser(self):
        cnt = 0
        if self.NameValidation(str(self.UserNameLog_2.text())):
            self.UserNameLog_2.setStyleSheet("border:1px solid rgb(94, 242, 255);")
            cnt += 1

        else:
            self.UserNameLog_2.setStyleSheet("border:1px solid rgb(255, 61, 61);")

        if self.PassWordValidation(str(self.UserpassLog_2.text())):
            self.UserpassLog_2.setStyleSheet("border:1px solid rgb(94, 242, 255);")
            cnt += 1
        else:
            self.UserpassLog_2.setStyleSheet("border:1px solid rgb(255, 61, 61)")

    def AddUser(self):
        cnt = 0
        if self.NameValidation(str(self.UserNameLog_3.text())):
            self.UserNameLog_3.setStyleSheet("border:1px solid rgb(94, 242, 255);")
            cnt += 1
        else:
            self.UserNameLog_3.setStyleSheet("border:1px solid rgb(255, 61, 61);")

        if self.PassWordValidation(str(self.UserpassLog_3.text())) and self.PassWordValidation(str(self.UserpassLog_4.text())):
            if str(self.UserpassLog_3.text()) == str(self.UserpassLog_4.text()):
                self.UserpassLog_3.setStyleSheet("border:1px solid rgb(94, 242, 255);")
                self.UserpassLog_4.setStyleSheet("border:1px solid rgb(94, 242, 255);")
                cnt += 1
            else:
                self.UserpassLog_3.setStyleSheet("border:1px solid rgb(255, 61, 61);")
                self.UserpassLog_4.setStyleSheet("border:1px solid rgb(255, 61, 61);")
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Error Message")
                msgBox.setText("Password does not match the confirm password.");
                msgBox.setInformativeText(" Type both passwords again. ")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);
                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Ok:
                    self.UserpassLog_2.setStyleSheet("border:1px solid rgb(255, 61, 61)")

        if cnt == 2:
            if self.LogIN(str(self.UserNameLog_3.text()), str(self.UserpassLog_4.text())):
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Error Message")
                msgBox.setText("the name you entered is already exists");
                msgBox.setInformativeText("Please use another name")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);
                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Ok:
                    self.UserpassLog_3.clear()
                    self.UserpassLog_4.clear()
            else:
                self.InsertUser(str(self.UserNameLog_3.text()),str(self.UserpassLog_4.text()))
                self.comboBox.addItem(str(self.UserNameLog_3.text()))
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Information)
                msgBox.setWindowTitle("successful operation")
                msgBox.setText("Adding new user done successfully ");
                msgBox.setInformativeText("you can access the program with the new user now")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);
                self.UserNameLog_3.setStyleSheet("")
                self.UserpassLog_3.setStyleSheet("")
                self.UserpassLog_4.setStyleSheet("")
                pygame.mixer.music.load("sounds/addingdone.mp3")
                pygame.mixer.music.play()
                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Ok:
                    self.UserpassLog_3.clear()
                    self.UserpassLog_4.clear()
                    self.UserNameLog_3.clear()
                    self.stackedWidget.setCurrentIndex(1)

    def DeleteUser(self):
        name  = str(self.comboBox.currentText())
        cnt = 0
        if len(name) == 0:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setWindowTitle("Deleting Error")
            msgBox.setText("there is no users in database ");
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save);
            ret = msgBox.exec_();
            if ret == QtGui.QMessageBox.Ok:
                self.comboBox.setStyleSheet("border:1px solid rgb(255, 61, 61)")
        else:
            self.comboBox.setStyleSheet("border:1px solid rgb(94, 242, 255);")
            cnt += 1
        n , p = self.mangerValidation("admin" , str(self.UserpassLog_5.text()))
        if p == 1:
            cnt += 1
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle("Error")
            msgBox.setText(" Incorrect password");
            msgBox.setInformativeText("Please try again !")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save);

            ret = msgBox.exec_();
            if ret == QtGui.QMessageBox.Ok:
                self.UserpassLog_5.setStyleSheet("border:1px solid rgb(255, 61, 61)")
        if cnt == 2:
            self.comboBox.setStyleSheet("")
            self.UserpassLog_5.setStyleSheet("")
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setWindowTitle("successful Deleteing")
            msgBox.setText("Deleting user done successfully ");
            msgBox.setInformativeText("user is no longer in database")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save);
	    pygame.mixer.music.load("sounds/deletingdone.mp3")
   	    pygame.mixer.music.play()
            ret = msgBox.exec_();
            if ret == QtGui.QMessageBox.Ok:
		self.comboBox.setStyleSheet("")
		self.UserpassLog_5.setStyleSheet("")
                self.deleteUser(str(self.comboBox.currentText()))
                self.UserpassLog_5.clear()
                n = self.comboBox.currentIndex()
                self.comboBox.removeItem(n)
                self.stackedWidget.setCurrentIndex(1)



a = QtGui.QApplication(sys.argv)
m = Mangersetup()
a.exec_()
