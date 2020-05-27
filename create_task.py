# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_task.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3, random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox

class CommonHelper:
    def __init__(self):
        pass
    @staticmethod
    def readQss(style):
        with open(style,'r') as f:
            return f.read()

class Create_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(455, 595)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        #self.label_3.setGeometry(QtCore.QRect(60, 160, 81, 31))
        ##########
        self.label_3.setGeometry(QtCore.QRect(60, 150, 111, 31))
        ##########
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 111, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 260, 91, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(60, 340, 81, 21))
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(150, 300, 141, 31))
        self.radioButton.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 100, 222, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 150, 222, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 200, 222, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 250, 222, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 370, 351, 151))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setEnabled(0)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 540, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #########################
        self.pushButton.clicked.connect(self.createOrder)
        #########################

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "创建订单页面"))
        self.label.setText(_translate("Form", "创建新的订单"))
        self.label_2.setText(_translate("Form", "物品名称"))
        self.label_3.setText(_translate("Form", "物品总重(kg)"))
        self.label_4.setText(_translate("Form", "物品发送时间"))
        self.label_5.setText(_translate("Form", "接收方名称"))
        self.label_6.setText(_translate("Form", "特殊要求"))
        self.radioButton.setText(_translate("Form", "其他要求"))
        self.pushButton.setText(_translate("Form", "提交"))
    
    #########################
    def createOrder(self):
        tmpFile = open(r'tmp.txt', 'r')
        Csender = tmpFile.readline()
        tmpFile.close()

        Cname = self.lineEdit.text()
        Cweight = float(self.lineEdit_2.text())
        Ctime = self.lineEdit_3.text()
        Treceiver = self.lineEdit_4.text()
        SPRequired = self.radioButton.isChecked()
        SPstring = self.textEdit.toPlainText()
        if Cname == '' or Cweight == '' or Ctime == '' or Treceiver == '':
            reply=QMessageBox.information(self,'提示','各项不能为空！')
            return

        co = sqlite3.connect(r'Data.db')
        cu = co.cursor()
        cu.execute("SELECT ID FROM order_")
        
        idlist = cu.fetchall()
        for i in range(len(idlist)):
            idlist[i] = int(idlist[i][0])
        if len(idlist) == 0:
            ID = 1
        else:
            ID = max(idlist) + 1
        ID = str(ID).zfill(6)

        cu.execute("INSERT INTO order_ VALUES('{t0}', '{t1}', {t2}, '{t3}', '{t4}', {t5}, '{t6}', '{t7}', {t8});".format(t0 = ID, t1 = Cname, t2 = Cweight, t3 = Ctime, t4 = Treceiver, t5 = SPRequired, t6 = SPstring, t7 = Csender, t8 = 0))
        co.commit()
        cu.close()
        co.close()

        reply=QMessageBox.information(self,'提示','创建订单成功！')
        return
    #########################

