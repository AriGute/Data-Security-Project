# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverGui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import ChatApp.server as ca


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.server = ca.Server()

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(280, 160)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.startServer = QtWidgets.QPushButton(self.centralwidget)
        self.startServer.setGeometry(QtCore.QRect(100, 110, 81, 31))
        self.startServer.setObjectName("startServer")
        self.startServer.clicked.connect(self.runServer)

        self.addUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.addUserButton.setGeometry(QtCore.QRect(100, 80, 81, 21))
        self.addUserButton.setObjectName("addUserButton")
        self.addUserButton.clicked.connect(self.addUser)

        self.addUserText = QtWidgets.QLabel(self.centralwidget)
        self.addUserText.setGeometry(QtCore.QRect(10, 0, 241, 16))
        self.addUserText.setObjectName("addUserText")

        self.user_name = QtWidgets.QLabel(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.user_name.setObjectName("user_name")

        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(10, 40, 51, 31))
        self.password.setObjectName("password")

        self.userBox = QtWidgets.QLineEdit(self.centralwidget)
        self.userBox.setGeometry(QtCore.QRect(80, 20, 151, 21))
        self.userBox.setObjectName("userBox")

        self.passwordBox = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordBox.setGeometry(QtCore.QRect(80, 50, 151, 21))
        self.passwordBox.setObjectName("passwordBox")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 279, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startServer.setText(_translate("MainWindow", "Start Server"))
        self.addUserButton.setText(_translate("MainWindow", "Add new User"))
        self.addUserText.setText(_translate("MainWindow", "Add new user to the data base:"))
        self.user_name.setText(_translate("MainWindow", "User name:"))
        self.password.setText(_translate("MainWindow", "Password:"))


    def runServer(self):
        # disable buttons and text.
        self.addUserButton.setEnabled(False)

        self.addUserText.setEnabled(False)

        self.user_name.setEnabled(False)
        self.userBox.setEnabled(False)

        self.password.setEnabled(False)
        self.passwordBox.setEnabled(False)

        self.startServer.setEnabled(False)
        # disable buttons and text.

        self.server.StartServer()

    def addUser(self):
        print("add user\n")
        name = self.userBox.displayText()
        password = self.passwordBox.displayText()
        user = (name, password)
        print(user)
        # self.server.experemential()
        self.server.AddUser(user)

if __name__ == "__main__":
    sys._excepthook = sys.excepthook
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
    sys.excepthook = exception_hook

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
