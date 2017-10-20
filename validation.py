from PyQt4 import QtGui , QtCore


class validation:
    def __init__(self):
        pass

    def NameValidation(self,text):
        specialChars = "1234567890-_+-*/.~!@#$%^&*()_+?><{}[],"

        if len(text) == 0 or len(text) <= 3 or len(text) > 50:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle("Invaild name")
            msgBox.setText("name is too short or too long");
            msgBox.setInformativeText("it must be in range 3 to 50 characters !")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save);
            ret = msgBox.exec_();
            if ret == QtGui.QMessageBox.Ok:
                pass
            return False
        for ch in text:
            if ch in specialChars:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Invaild name")
                msgBox.setText("name contains non-characters");
                msgBox.setInformativeText("Please use only letters(a-z)")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);
                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Ok:
                    pass
                return False
        return True

    def NidValidation(self,text):
        Num = "1234567890"
        if len(text) == 0 or len(text) <= 3 or len(text) > 14:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle("Invaild National ID")
            msgBox.setText("NID is too short or too long");
            msgBox.setInformativeText("it must be in range 14 to 20 Number ")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save);
            ret = msgBox.exec_();
            if ret == QtGui.QMessageBox.Ok:
                pass
            return False
        for n in text:
            if not n in Num:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Invaild National")
                msgBox.setText("NID contains non-characters");
                msgBox.setInformativeText("Please use only Numbers(0-9)")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);
                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Ok:
                    pass
                return  False
        return True

    def PassWordValidation(self,text):
        specialChars = "-_+-*/.~!@#$%^&*()_+?><{}[],"
        if len(text) == 0 or len(text) <= 3 or len(text) > 50:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle("Invaild Password")
            msgBox.setText("Password is too short or too long");
            msgBox.setInformativeText("it must be in range 3 to 50 characters !")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save);
            ret = msgBox.exec_();
            if ret == QtGui.QMessageBox.Ok:
                pass
            return False
            return False
        for ch in text:
            if ch in specialChars:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Invaild Password")
                msgBox.setText("Password contains non-characters");
                msgBox.setInformativeText("Please use only letters(a-z) or numbers(0-9) ")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);
                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Ok:
                    pass
                return False
        return True

    def mangerValidation(self,name,password):
        if not name == "admin":
            n = 0
        else:
            n = 1

        if not password == "admin":
            p = 0
        else:
            p = 1
        return n ,p


