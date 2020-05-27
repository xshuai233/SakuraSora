# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QStandardItemModel
# from PyQt5.QtWidgets import QHeaderView
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


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(800, 600)
        self.tableView = QtWidgets.QTableView(widget)
        self.tableView.setGeometry(QtCore.QRect(10, 170, 771, 411))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(660, 20, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(widget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 20, 121, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        ##################
        self.pushButton_4 = QtWidgets.QPushButton(widget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 70, 121, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.reflush)
        self.pushButton.clicked.connect(self.confirm)
        ##################
        self.model = QStandardItemModel(160, 4)
        self.model.setHorizontalHeaderLabels(['订单编号', '物品名称', '物品总重(kg)', '物品发送时间', '发送方名称','接收方名称','订单状态'])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

        self.mx = 0

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.pushButton.setText(_translate("widget", "订单结束确认"))
        self.pushButton_3.setText(_translate("widget", "返回前一页面"))
        self.pushButton_4.setText(_translate("Form", "刷新"))
        styleFile = './style1.qss'
        qssStyle = CommonHelper.readQss(styleFile)
        widget.setStyleSheet(qssStyle)

    ####刷新代码可以写，也可以不写
    #####在这里写订单的确认
    #################
    def reflush(self):
        QApplication.processEvents()

        tmpFile = open(r'tmp.txt', 'r')
        user = tmpFile.readline()
        tmpFile.close()

        co = sqlite3.connect(r'Data.db')
        cu = co.cursor()
        cu.execute("SELECT isLogi FROM user WHERE username='{tmp}';".format(tmp = user))
        flag = cu.fetchone()[0]
        #cu.execute("SELECT ID, Cname, Cweight, Ctime, Csender, isCanceled FROM order_ WHERE Treceiver='{tmp}';".format(tmp = user))
        cu.execute("SELECT ID, Cname, Cweight, Ctime, Csender, Treceiver, isCanceled FROM order_;")
        result = cu.fetchall()
        cu.close()
        co.close()

        if not flag:
            reply=QMessageBox.information(self,'提示','您所在的公司不属于物流公司！')
            return
        
        if len(result) > self.mx:
            self.mx = len(result)

        for i in range(len(result)):
            for j in range(7):
                if j == 2:
                    item = QStandardItem(str(result[i][j]))
                elif j == 6:
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

    #################

    #################
    def confirm(self):
        tmpFile = open(r'tmp.txt', 'r')
        user = tmpFile.readline()
        tmpFile.close()

        co = sqlite3.connect(r'Data.db')
        cu = co.cursor()
        cu.execute("SELECT isLogi FROM user WHERE username='{tmp}';".format(tmp = user))
        result = cu.fetchone()[0]
        cu.close()
        co.close()

        if not result:
            reply=QMessageBox.information(self,'提示','您所在的公司不属于物流公司！')
            return

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
            
            if flag == 0:
                cu.execute("UPDATE order_ SET isCanceled = 4 WHERE ID = '{t0}';".format(t0 = ID))
                co.commit()
            elif flag == 1 or flag == 2: 
                reply=QMessageBox.information(self,'提示','您所选择的订单已被挂起，无法完成！')
                flag2 = False
            elif flag == 3:
                reply=QMessageBox.information(self,'提示','您所选择的订单已被撤销，无法完成！')
                flag2 = False
        cu.close()
        co.close()

        if flag2:
            reply=QMessageBox.information(self,'提示','所选订单已完成！')
            self.reflush()
        #################