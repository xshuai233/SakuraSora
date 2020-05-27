# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'merchant.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import QModelIndex
#from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CommonHelper:
    def __init__(self):
        pass
    @staticmethod
    def readQss(style):
        with open(style,'r') as f:
            return f.read()

class Merchant_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(665, 20, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(665, 70, 121, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 20, 121, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(15, 170, 771, 411))
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(15, 70, 121, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableView.setObjectName("tableView")
        self.model=QStandardItemModel(160,4)
        self.model.setHorizontalHeaderLabels(['订单编号','物品名称','物品总重(kg)','物品发送时间','接收方名称','订单状态'])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        ##############
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        ##############
        self.pushButton_4.clicked.connect(self.reflush)
        ##############
        self.pushButton_2.clicked.connect(self.removeOrder)
        ##############
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        ##############
        self.mx = 0
        ##############
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "商家页面"))
        self.pushButton.setText(_translate("Form", "创建新订单"))
        self.pushButton_2.setText(_translate("Form", "撤销订单"))
        self.pushButton_3.setText(_translate("Form", "返回前一页面"))
        self.pushButton_4.setText(_translate("Form", "刷新"))
        styleFile = './style1.qss'
        qssStyle = CommonHelper.readQss(styleFile)
        Form.setStyleSheet(qssStyle)

    def getItemAtRow(self):
        return self.tableView.currentIndex().row()

    def reflush(self):
        QApplication.processEvents()

        ##############
        tmpFile = open(r'tmp.txt', 'r')
        user = tmpFile.readline()
        tmpFile.close()

        co = sqlite3.connect(r'Data.db')
        cu = co.cursor()
        cu.execute("SELECT ID, Cname, Cweight, Ctime, Treceiver, isCanceled FROM order_ WHERE Csender='{tmp}';".format(tmp = user))
        result = cu.fetchall()
        cu.close()
        co.close()

        if len(result) > self.mx:
            self.mx = len(result)

        for i in range(len(result)):
            for j in range(6):
                if j == 2:
                    item = QStandardItem(str(result[i][j]))
                elif j == 5:
                    #0代表初始，1代表发出方挂起，2代表接受方挂起，3代表已撤销，4代表已完成
                    if result[i][j] == 0:
                        s = '已发起'
                    elif result[i][j] == 1 or result[i][j] == 2:
                        s = '已挂起'
                    elif result[i][j] == 3:
                        s = '已撤销'
                    else:
                        s = '已完成'
                    item = QStandardItem(s)
                else:
                    item = QStandardItem(result[i][j])
                self.model.setItem(i, j, item)
        
        if self.mx > len(result):
            for i in range(len(result), self.mx):
                for j in range(5):
                    item = QStandardItem('')
                    self.model.setItem(i, j, item)
            self.mx = len(result)
        
        ##############
    
    ################
    def removeOrder(self):
        indexs=self.tableView.selectionModel().selection().indexes()
        rows = []
        for index in indexs:
            if index.row() not in rows:
                rows.append(index.row())

        co = sqlite3.connect(r'Data.db')
        cu = co.cursor()
        
        flag2 = True

        for i in rows:
            ID = self.model.index(i, 0).data()
            if ID is None:
                continue
            cu.execute("SELECT isCanceled FROM order_ WHERE ID = '{t0}';".format(t0 = ID))
            flag = cu.fetchone()
            if flag is None:
                continue
            else:
                flag = flag[0]
            # print(flag)
            if flag == 0:
                cu.execute("UPDATE order_ SET isCanceled = 1 WHERE ID = '{t0}';".format(t0 = ID))
                co.commit()
            elif flag == 2:
                #cu.execute("DELETE FROM order_ WHERE ID = '{t0}';".format(t0 = ID))
                cu.execute("UPDATE order_ SET isCanceled = 3 WHERE ID = '{t0}';".format(t0 = ID))
                co.commit()
            elif flag == 4:
                reply=QMessageBox.information(self,'提示','您所选择的订单已完成，无法撤销！')
                flag2 = False

        cu.close()
        co.close()

        if flag2:
            reply=QMessageBox.information(self,'提示','所选订单已挂起/撤销！')
            self.reflush()
    ################