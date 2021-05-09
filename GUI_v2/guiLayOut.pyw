# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiLayOut.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys

import ChatApp.client as cc


class Ui_MainWindow(cc.Client):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(450, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(340, 330, 101, 31))
        self.sendButton.setObjectName("sendButton")
        self.sendButton.clicked.connect(self.SendMsg)

        self.conversationBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.conversationBox.setGeometry(QtCore.QRect(130, 30, 311, 271))
        self.conversationBox.setObjectName("conversationBox")

        self.msgBox = QtWidgets.QTextEdit(self.centralwidget)
        self.msgBox.setGeometry(QtCore.QRect(10, 330, 321, 31))
        self.msgBox.setObjectName("msgBox")

        self.ipBox = QtWidgets.QLineEdit(self.centralwidget)
        self.ipBox.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.ipBox.setObjectName("ipBox")
        self.ipBox.setText('localhost')

        self.portBox = QtWidgets.QLineEdit(self.centralwidget)
        self.portBox.setGeometry(QtCore.QRect(10, 70, 101, 20))
        self.portBox.setObjectName("portBox")
        self.portBox.setText("5023")

        self.nameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.nameBox.setGeometry(QtCore.QRect(10, 140, 101, 20))
        self.nameBox.setObjectName("nameBox")
        self.nameBox.setText('name')

        self.passBox = QtWidgets.QLineEdit(self.centralwidget)
        self.passBox.setGeometry(QtCore.QRect(10, 160, 101, 20))
        self.passBox.setObjectName("password")
        self.passBox.setText('password')

        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(10, 180, 101, 31))
        self.connectButton.setObjectName("connectButton")
        self.connectButton.clicked.connect(self.startClient)

        self.ipLabel = QtWidgets.QLabel(self.centralwidget)
        self.ipLabel.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.ipLabel.setObjectName("ipLabel")


        self.conversationLabel = QtWidgets.QLabel(self.centralwidget)
        self.conversationLabel.setGeometry(QtCore.QRect(130, 10, 91, 16))
        self.conversationLabel.setObjectName("conversationLabel")

        self.portLabel = QtWidgets.QLabel(self.centralwidget)
        self.portLabel.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.portLabel.setObjectName("portLabel")

        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.nameLabel.setObjectName("nameLabel")

        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setGeometry(QtCore.QRect(10, 310, 91, 16))
        self.messageLabel.setObjectName("messageLabel")

        # self.conversationScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        # self.conversationScrollBar.setGeometry(QtCore.QRect(420, 30, 20, 271))
        # self.conversationScrollBar.setOrientation(QtCore.Qt.Vertical)
        # self.conversationScrollBar.setObjectName("conversationScrollBar")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.ipBox.setReadOnly(True)
        self.portBox.setReadOnly(True)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def startClient(self):
        self.nameBox.setReadOnly(True)
        self.connectButton.setDisabled(True)

        self.BindMessageFunction(self.PostMsg, self.ForceQuit)
        self.StartClient(self.nameBox.displayText(), self.passBox.displayText())



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.ipLabel.setText(_translate("MainWindow", "ip adress:"))
        self.conversationLabel.setText(_translate("MainWindow", "conversation:"))
        self.portLabel.setText(_translate("MainWindow", "port number:"))
        self.nameLabel.setText(_translate("MainWindow", "User login:"))
        self.messageLabel.setText(_translate("MainWindow", "message box:"))

    def PostMsg(self, msg=""):
        self.conversationBox.append(msg)


    def SendMsg(self):
        # pass a message to the conversation box.
        msg = self.msgBox.toPlainText()
        self.msgBox.setText("")
        if self.SendMessagFunc == '':
            print("Message function must be binding first.")
            sys.exit(self.exec_())
        else:
            pass
            # self.PostMsg(msg)
            self.send(msg)

    def ForceQuit(self):
        QtCore.QCoreApplication.quit()

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
