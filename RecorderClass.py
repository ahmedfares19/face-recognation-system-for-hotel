from PyQt4 import  QtCore ,QtGui
import sys , time
sys.path.append("/usr/local/lib/python2.7/site-packages")
import cv2
import os,pygame
import shutil
from threading import Thread

class QCustomSignal(QtCore.QObject):
    takingDataSetFinshed = QtCore.pyqtSignal([str])

class QfaceSignal(QtCore.QObject):
    numofface = QtCore.pyqtSignal([str])

class QRecorderClass:
    def __init__(self , imageWindow  , storedImagePath ,
                 NoOfImages = 50, camIndex = 0 , samplingRate =10 ):
        self._imageWindow = imageWindow
        self._storedImagePath = storedImagePath
        self._NoOfImages = NoOfImages
        self._camIndex = camIndex
        self._samplingTime = int(1000/samplingRate)
        self.camObject = None
        self.imageCounts = 0
        self.RecorderTimer = QtCore.QTimer()
        self.timevoice = QtCore.QTimer()
        self.timevoice.timeout.connect(self.thre)
        self.timevoice.setInterval(100)
        self.timevoice.start()
        self.RecorderTimer.timeout.connect(self.TakeNewImage)
        self.temp = QCustomSignal()
        self.numoffaces = 1
        pygame.init()
    def thre(self):
        self.t1 = Thread(target=self.Qvoice)
        self.t1.start()
    def Qvoice(self):
        self.timevoice.stop()
        if self.numoffaces == 0 and self.imageCounts < self._NoOfImages:
            pygame.mixer.music.load("sounds/noperson.mp3")
            pygame.mixer.music.play()
        if self.numoffaces > 1 and self.imageCounts < self._NoOfImages:
            pygame.mixer.music.load("sounds/manyperson.mp3")
            pygame.mixer.music.play()
        self.timevoice.start(4500)

    def TakeNewImage(self):
        self.RecorderTimer.stop()
        ret , image = self.camObject.read()
        if ret :
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.FaceObjectClassifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(80, 80))
            self.numoffaces = len(faces)

            for x, y, w, h in faces:
                subImage = gray[y:y+h, x :x+w ]
                resizedImage = cv2.resize(subImage , (168 , 192))
                if self.numoffaces == 1:
                    imagePath = os.path.join(self._storedImagePath, "image_{}.png".format(self.imageCounts))
                    self.imageCounts +=1
                    cv2.imwrite(imagePath, resizedImage )
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 1)
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            colored = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            qImg = QtGui.QImage(colored.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
            piximage = QtGui.QPixmap(qImg)
            self._imageWindow.setPixmap(piximage)
            if self.imageCounts>= self._NoOfImages :
                self.EndRecording()
            else:
                self.RecorderTimer.start(self._samplingTime)




    def Record(self):
        self.imageCounts = 0
        try:
            self.camObject = cv2.VideoCapture(self._camIndex)
            self.FaceObjectClassifier = cv2.CascadeClassifier(os.path.join( "Classifiers", "FaceDetection.xml"))

            if not os.path.isdir(self._storedImagePath):
                os.mkdir(self._storedImagePath)
                self.RecorderTimer.start(self._samplingTime)
            else:
                msgBox= QtGui.QMessageBox()
                msgBox.setText("this ID is already exist.");
                msgBox.setInformativeText("Do you want to overwrite the existing id?")
                msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No )
                msgBox.setDefaultButton(QtGui.QMessageBox.Save);
                ret = msgBox.exec_();
                if ret == QtGui.QMessageBox.Yes :
                    shutil.rmtree(self._storedImagePath)
                    os.mkdir(self._storedImagePath)
                    self.RecorderTimer.start(self._samplingTime)
                if ret == QtGui.QMessageBox.No:
                    pass
        except Exception as e :
            print (e)
    def EndRecording(self):

        self.camObject.release()
        tempPixMap = QtGui.QPixmap(os.path.join( self._storedImagePath,'image_24.png'))
        self._imageWindow.setPixmap(tempPixMap)
        path, file = os.path.split(self._storedImagePath)
        self.temp.takingDataSetFinshed.emit(self._storedImagePath)


