# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1116, 600)
        self.labImage = QtWidgets.QLabel(Dialog)
        self.labImage.setGeometry(QtCore.QRect(20, 0, 411, 391))
        self.labImage.setObjectName("labImage")
        self.btnOpen = QtWidgets.QPushButton(Dialog)
        self.btnOpen.setGeometry(QtCore.QRect(30, 470, 181, 31))
        self.btnOpen.setObjectName("btnOpen")
        self.btnConvert = QtWidgets.QPushButton(Dialog)
        self.btnConvert.setGeometry(QtCore.QRect(30, 500, 181, 31))
        self.btnConvert.setObjectName("btnConvert")
        self.btnSave = QtWidgets.QPushButton(Dialog)
        self.btnSave.setGeometry(QtCore.QRect(30, 530, 181, 31))
        self.btnSave.setObjectName("btnSave")
        self.convmage = QtWidgets.QLabel(Dialog)
        self.convmage.setGeometry(QtCore.QRect(560, 10, 421, 381))
        self.convmage.setObjectName("convmage")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labImage.setText(_translate("Dialog", "TextLabel"))
        self.btnOpen.setText(_translate("Dialog", "Open"))
        self.btnConvert.setText(_translate("Dialog", "Convert image"))
        self.btnSave.setText(_translate("Dialog", "Save"))
        self.convmage.setText(_translate("Dialog", "TextLabel"))
