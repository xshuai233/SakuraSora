# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header

import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex, QAbstractItemModel
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QLineEdit


class CommonHelper:
    def __init__(self):
        pass
    @staticmethod
    def readQss(style):
        with open(style,'r') as f:
            return f.read()

class Ui_RegisterWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 391, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 91, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 91, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 229, 111, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 280, 91, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.radioButton=QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(170,350,115,19))
        self.radioButton.setObjectName("radioButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 400, 72, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 480, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 110, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 170, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 230, 221, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 280, 221, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 400, 113, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 400, 93, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 480, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.hide)
        self.pushButton_3.clicked.connect(self.return_zero)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #########################
        self.pushButton.clicked.connect(self.register_)
        self.pushButton_2.clicked.connect(self.sendEmail)
        #########################


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "注册"))
        self.label_2.setText(_translate("MainWindow", "用户名字"))
        self.label_3.setText(_translate("MainWindow", "用户密码"))
        self.label_4.setText(_translate("MainWindow", "注册公司名字"))
        self.label_5.setText(_translate("MainWindow", "企业邮箱"))
        self.label_6.setText(_translate("MainWindow", "验证码"))
        self.radioButton.setText(_translate("MainWindow","为物流公司"))
        self.pushButton.setText(_translate("MainWindow", "注册"))
        self.pushButton_2.setText(_translate("MainWindow", "发送"))
        self.pushButton_3.setText(_translate("MainWindow", "取消"))
        styleFile = './style1.qss'
        qssStyle = CommonHelper.readQss(styleFile)
        MainWindow.setStyleSheet(qssStyle)

    def return_zero(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")

    #########################
    def sendEmail(self):
        receiver = self.lineEdit_4.text()
        if receiver == '':
            reply=QMessageBox.information(self,'提示','邮箱不能为空！')
            return

        msg_from = '1599516703@qq.com'
        passwd = 'gsymxhoheoojiaie'
        msg_to = receiver

        subject = '樱空物流验证'
        self.code = ''
        for i in range(6):
            self.code = self.code + str(random.randint(0, 9))

        msg = MIMEText('您本次的验证码为：' + self.code)
        msg['Subject'] = '樱空物流验证'
        msg['From'] = msg_from
        msg['To'] = msg_to

        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
        except:
            reply=QMessageBox.information(self,'提示','发送失败！可能原因为邮箱格式错误。')
        finally:
            s.quit()

    def register_(self):
        co = sqlite3.connect(r'Data.db')
        cu = co.cursor()
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        companyname = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        verCode = self.lineEdit_5.text()
        # print(username, password, companyname, email)

        cu.execute("SELECT count(*) FROM user WHERE username='{tmp}';".format(tmp = username))
        result = cu.fetchone()[0]

        if username == '' or password == '' or companyname == '' or email == '' or verCode == '':
            reply=QMessageBox.information(self,'提示','各项不能为空！')
            cu.close()
            co.close()
            return 

        if result != 0:
            reply=QMessageBox.information(self,'提示','用户名已存在！')
            cu.close()
            co.close()
            return
        
        if verCode != self.code:
            reply=QMessageBox.information(self,'提示','验证码错误！')
            cu.close()
            co.close()
            return
        
        cu.execute("INSERT INTO user VALUES('{t1}', '{t2}', '{t3}', '{t4}', {t5});".format(t1 = username, t2 = password, t3 = companyname, t4 = email, t5 = self.radioButton.isChecked()))
        co.commit()
        cu.close()
        co.close()
        reply=QMessageBox.information(self,'提示','注册成功！')
        return
    #########################


