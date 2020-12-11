import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from IPython.external.qt_for_kernel import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog

from interface import Ui_Dialog

IMAGE_SIZE = 500

class LabApp(QMainWindow, QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.btnOpen.clicked.connect(self.browser_folder)

    # открыть файл для обработки
    def browser_folder(self):
        file_path = self.get_file_path()
        print(file_path)
        self.load_image(self.labImage, file_path)

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


