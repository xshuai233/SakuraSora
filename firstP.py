# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new-face.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox

class Face_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)
        self.Label=QtWidgets.QLabel(MainWindow)
        self.Label.setGeometry(QtCore.QRect(0,0,798,600))
        self.Label.setStyleSheet("border-image:url(./img/9.jpg)")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 300, 266))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton:hover{border-image:url(./img/3.png)}")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 170, 300, 266))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton:hover{border-image:url(./img/4.png)}")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 340, 300, 266))
        self.pushButton_3.setText("")
        self.pushButton_3.setStyleSheet("QPushButton:hover{border-image:url(./img/5.png)}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 570, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        ###################
        #self.pushButton_3.clicked.connect(self.text)
        ###################

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(90, 270, 72, 15))
        self.label.setStyleSheet("color:rgb(255,0,153);font-weight:bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(350, 440, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:rgb(255,0,153);font-weight:bold;")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(640, 320, 72, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color:rgb(255,0,153);font-weight:bold;")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton_4.setText(_translate("MainWindow", "登出"))
        self.label.setText(_translate("MainWindow", "我是商家"))
        self.label_2.setText(_translate("MainWindow", "我是客户"))
        self.label_3.setText(_translate("MainWindow", "我是物流"))