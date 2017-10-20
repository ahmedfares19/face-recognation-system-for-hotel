import os
import exceptions
import cv2
import numpy as np
from PyQt4 import  QtCore
class QCustomSignal(QtCore.QObject):
    TrainingFinshed = QtCore.pyqtSignal([str])
class QTrainer(QtCore.QThread):
    def __init__(self , user_id_path , MinImages = 10):
        QtCore.QThread.__init__(self)
        self.__ID = user_id_path
        self.TrainingSignal = QCustomSignal()
        #validation
        if(not os.path.isdir(self.__ID)):
            raise exceptions.BaseException("pls provide valid path")
        self.allawableFormates = ["png" , "pgm"]
        counter = 0
        for file in os.listdir(self.__ID):
            temp = file.split(".")
            if(temp[-1] in self.allawableFormates):
                counter += 1

        if counter < MinImages:
            raise exceptions.ValueError("the minimum number of images must be > {}".format(MinImages))

    def run(self):
        print ("task started .....")
        Images = []
        Lables = []
        labelsNames = []

        #yale data
        yale_path = os.path.join(os.getcwd() , "FacesDataSet")
        for folder in os.listdir(yale_path):
            folderPath = os.path.join( yale_path , folder )
            for image_path in os.listdir(folderPath) :
                splitedFile = image_path.split(".")
                if splitedFile[-1] in self.allawableFormates:
                    image_abs_path = os.path.join(yale_path ,folder, image_path)
                    image = cv2.imread(image_abs_path, cv2.COLOR_BGR2GRAY)
                    Images.append(image)
                    Lables.append(len(labelsNames))
            labelsNames.append(folder)

        for image_path in os.listdir(self.__ID):
            splitedFile = image_path.split(".")
            if splitedFile[-1] in self.allawableFormates :
                print image_path
                image_abs_path = os.path.join( self.__ID , image_path )
                image = cv2.imread( image_abs_path , cv2.COLOR_BGR2GRAY)
                Images.append(image)
                Lables.append(len(labelsNames))
        path, file = os.path.split(self.__ID)
        labelsNames.append(file)
        trainLabels = np.asarray(Lables , dtype= np.int32 )
        print("training started.............")
        classifier  = cv2.face.createLBPHFaceRecognizer()
        classifier.train( Images , trainLabels )
        outputpath = os.path.join(os.getcwd() , "facesModels" , file+".xml" )
        classifier.save(outputpath)
        self.TrainingSignal.TrainingFinshed.emit(outputpath)
        print("training ended.............")








def __TEST__():
    temp  = QTrainer("/home/mohamed/codes/workProjects/python/hotel_registration/dataSet/123" )
    temp.Start()

if __name__ == "__main__":
    __TEST__()

