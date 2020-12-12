import os
import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import cv2
import numpy
from IPython.external.qt_for_kernel import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDialog
from PIL import Image
from interface import Ui_Dialog

IMAGE_SIZE = 500
FILE_PATH = ""

class LabApp(QMainWindow, QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.btnOpen.clicked.connect(self.browser_folder)
        self.btnConvert.clicked.connect(self.convertImage)
        self.btnSave.clicked.connect(self.save_Image)

    # открыть файл для обработки
    def browser_folder(self):
        FILE_PATH = self.get_file_path()
        print(FILE_PATH)
        # self.load_image(self.labImage, file_path)
        self.openFile(FILE_PATH)

    def save_Image(self):
        save_image =self.convmage
        if save_image is not None:
            image = self.getBytesFromPixmap(save_image.pixmap())
            image2 = self.scaledImage(image)

            date = str(datetime.datetime.now()).replace(":", '')
            print("save")
            date = date.replace('-', '')
            date = date.replace('.', '')
            date = date.replace(' ', '')

            # file_path = self.
            file_name = FILE_PATH + date + '.jpg'

            save_image.pixmap().save(file_name, 'jpg', 100)

    #получить ссылку на выбранный файл
    def get_file_path(self):
        Tk().withdraw()
        filepath = askopenfilename()
        return filepath

    #загрузить изображение по полученному пути
    #отобразить изображение
    def load_image(self, view, file_name):
        pixmap = QtGui.QPixmap(file_name)
        p = pixmap.scaled(IMAGE_SIZE, IMAGE_SIZE, QtCore.Qt.KeepAspectRatio)
        view.setPixmap(p)
        view.resize(IMAGE_SIZE, IMAGE_SIZE)

    #прочитать и отобразить оригинальный файл
    def openFile(self, file_name):
        if file_name:
            with open(file_name, "rb") as file:
                image = self.toNumpyBytes(file.read())
                self.showedImage(image, self.labImage)

    def scaledImage(self, image):
        size = image.shape
        step = image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        image2 = QImage(image, size[1], size[0], step, qformat)
        image2 = image2.rgbSwapped()
        return image2

    #масштабировать и отобразить файл
    def showedImage(self, image, view):
        image2 = self.scaledImage(image)

        pixmap = QPixmap.fromImage(image2)
        pixmap = pixmap.scaled(IMAGE_SIZE, IMAGE_SIZE, QtCore.Qt.KeepAspectRatio)

        view.setPixmap(pixmap)
        view.resize(IMAGE_SIZE, IMAGE_SIZE)

    #преобразование
    def convertImage(self):
        if self.labImage is not None:
            data_image = self.getBytesFromPixmap(self.labImage.pixmap())

            image = cv2.Canny(data_image, cv2.IMREAD_UNCHANGED, 100, 200)
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) \
                if len(image.shape) >= 3 else image

            blur = cv2.GaussianBlur(gray, (21, 21), 0, 0)
            image = cv2.divide(gray, blur, scale=256)
            self.showedImage(image, self.convmage)

    #получить массив байт из pixmap
    def getBytesFromPixmap(self, pixmap):
        ba = QtCore.QByteArray()
        buff = QtCore.QBuffer(ba)
        buff.open(QtCore.QIODevice.WriteOnly)
        ok = pixmap.save(buff, "PNG")
        assert ok
        pixmap_bytes = ba.data()
        return self.toNumpyBytes(pixmap_bytes)

    #преобразовать в массив байт numpy
    def toNumpyBytes(self, data):
        data = numpy.array(bytearray(data))
        image = cv2.imdecode(data, cv2.IMREAD_UNCHANGED)
        print(type(image))
        return image




