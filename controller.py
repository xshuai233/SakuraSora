import sys
import sqlite3
from PyQt5.QtCore import QModelIndex, QAbstractItemModel
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox
from Login import Ui_LoginWindow
from register import Ui_RegisterWindow
from firstP import *
from merchant import *
from create_task import *
from client import *
from flow import *
class CommonHelper:
    def __init__(self):
        pass
    @staticmethod
    def readQss(style):
        with open(style,'r') as f:
            return f.read()

class LoginWindow(QMainWindow,Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check)
        self.pushButton_3.clicked.connect(self.jump)
    def check(self):
        # if self.lineEdit.text()=='' and self.lineEdit_2.text()=='':
        #     self.facial=FacialWindow()
        #     self.close()
        #     self.facial.show()
        # else:
        #     reply=QMessageBox.information(self,'提示','用户名或密码错误！')
        
        # if self.lineEdit.text() == '':
        #     reply=QMessageBox.information(self,'提示','用户名为空！')
        #     return

        #########################
        if self.lineEdit.text() == '':
            reply=QMessageBox.information(self,'提示','用户名为空！')
            return

        co = sqlite3.connect(r'Data.db')
        cu = co.cursor()
        cu.execute("SELECT password FROM user WHERE username='{tmp}';".format(tmp = self.lineEdit.text()))
        result = cu.fetchone()
        cu.close()
        co.close()

        tmpFile = open(r'tmp.txt', 'w')
        tmpFile.writelines(self.lineEdit.text())
        tmpFile.close()

        if result is None or self.lineEdit_2.text() != result[0]:
            reply=QMessageBox.information(self,'提示','用户名或密码错误！')
        else:
            self.facial=FacialWindow()
            self.hide()
            self.facial.show()
        
        #########################
    def jump(self):
        self.register=RegisterWindow()
        self.register.show()

class RegisterWindow(QMainWindow,Ui_RegisterWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class FacialWindow(QDialog,Face_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.merchant)
        self.pushButton_2.clicked.connect(self.client)
        self.pushButton_3.clicked.connect(self.flow)
        self.pushButton_4.clicked.connect(self.ret)
    def merchant(self):
        self.M_W=MerchantWindow()
        self.hide()
        self.M_W.show()
    def client(self):
        self.C_W=ClientWindow()
        self.hide()
        self.C_W.show()
    def flow(self):
        self.F_W=FlowWindow()
        self.hide()
        self.F_W.show()
    def ret(self):
        self.L_W=LoginWindow()
        self.close()
        self.L_W.show()


class MerchantWindow(QDialog,Merchant_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create)
        self.pushButton_2.clicked.connect(self.retrieve)
        self.pushButton_3.clicked.connect(self.ret_facial)
        self.tableView.doubleClicked.connect(self.details)
    def create(self):
        self.C_W=CreateWindow()
        self.C_W.show()
    def ret_facial(self):
        self.hide()
        self.F_W=FacialWindow()
        self.F_W.show()
    def retrieve(self):
        pass
    def details(self):
        if self.getItemAtRow()=="":
            reply=QMessageBox.information(self,'提示','选择的行为空!')
        else:
            pass

class ClientWindow(QDialog,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.ret_facial)

    def ret_facial(self):
        self.hide()
        self.F_W=FacialWindow()
        self.F_W.show()

class CreateWindow(QDialog,Create_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton.toggled.connect(self.isactive)
    def isactive(self):
        if self.radioButton.isChecked():
            self.textEdit.setEnabled(1)
        else:
            self.textEdit.setText("")
            self.textEdit.setEnabled(0)

class FlowWindow(QDialog,Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.ret_facial)

    def ret_facial(self):
        self.hide()
        self.F_W=FacialWindow()
        self.F_W.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    login=LoginWindow()
    login.show()
    sys.exit(app.exec_())