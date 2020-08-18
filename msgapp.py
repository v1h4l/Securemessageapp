# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msgapp.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

#from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
import sys
import socket
import PyQt5.QtGui
from threading import Thread
try:
    from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
except ImportError as e:
    print (e)

PORT = 5555
BUFSIZE = 1024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host_name= socket.gethostname()
#HOST = socket.gethostbyname(host_name)
HOST = "127.0.0.1"
print(HOST)


def msg_box(title, data):
    w = QtWidgets.QWidget()
    QtWidgets.QMessageBox.information(w, title, data)


def app_version():
    msg_box("version", "10.0.0.1")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 607)
        MainWindow.setStyleSheet("")
        MainWindow.setMinimumSize(QtCore.QSize(424, 607))
        MainWindow.setMaximumSize(QtCore.QSize(424, 607))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.color = QtWidgets.QColorDialog()

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 60, 401, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")

        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 381, 371))
        self.listWidget.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 10, 391, 31))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(230, 0, 41, 31))
        self.label.setStyleSheet("font:9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.label_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(72, 0, 151, 31))
        self.lineEdit.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        # self.lineEdit.setValidator(QtGui.QIntValidator())
        self.lineEdit.setMaxLength(15)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(HOST)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(262, 0, 121, 31))
        self.lineEdit_2.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setMaxLength(1200)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(180, 520, 861, 501))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")

        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.client_send_message)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 10, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.clear_logs)
        self.pushButton_2.setToolTip("It will clear the conversation")

        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 460, 401, 61))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")

        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 0, 271, 61))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);""font: 75 10pt \"MS Shell Dlg 2\";")
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 101, 51))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
        self.menubar.setObjectName("menubar")

        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionApp_Version = QtWidgets.QAction(MainWindow)
        self.actionApp_Version.setObjectName("actionApp_Version")
        self.actionApp_Version.triggered.connect(app_version)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(sys.exit)

        self.menuMenu.addAction(self.actionApp_Version)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nick:"))
        self.label_2.setText(_translate("MainWindow", "Ip Address"))
        self.pushButton.setText(_translate("MainWindow", "Send Message"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear Logs"))

        self.label_3.setText(_translate("MainWindow", "Enter message>"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionApp_Version.setText(_translate("MainWindow", "App Version"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def clear_logs(self):
        self.listWidget.clear()

    # def start_client(self):
    #    HOST = self.lineEdit.text()
     #   print(socket.gethostbyname(HOST))

    def client_send_message(self):

        ip_address = self.lineEdit.text()
        nick = self.lineEdit_2.text()
        nick = nick.replace('#>>', '')
        rmessage = self.textEdit_2.toPlainText()
        rmessage = rmessage.replace('#>>', '')

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((HOST, PORT))
        except:
            msg_box("connection", "connection refused")
            rmsg = nick + " #>> " + "not connected"
            self.listWidget.addItem(rmsg)
            return

        rmsg = nick + " #>> " + rmessage
        msg_box("connection", "connected")
        self.listWidget.addItem(rmsg)
        self.textEdit_2.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
#       self.pushButton_3.setGeometry(QtCore.QRect(60, 553, 81, 31))
#        self.pushButton_3.setObjectName("pushButton_3")
#        self.pushButton_3.clicked.connect(self.connect)
#  self.pushButton_3.setText(_translate("MainWindow", "connect"))
"""
self.actionOpen = QtWidgets.QAction(MainWindow)
self.actionOpen.setObjectName("open")
self.actionOpen.triggered.connect(saveAs)

self.actionSave = QtWidgets.QAction(MainWindow)
self.actionSave.setObjectName("Save")
# self.actionSave.triggered.connect(saveAs)

self.actionSaveAs = QtWidgets.QAction(MainWindow)
self.actionSaveAs.setObjectName("Saveas")
#self.actionOpen.triggered.connect(saveAs)        

self.menuMenu.addAction(self.actionOpen)
self.menuMenu.addAction(self.actionSave)
self.menuMenu.addAction(self.actionSaveAs)

self.actionOpen.setText(_translate("MainWindow", "Open"))
self.actionSave.setText(_translate("MainWindow", "Save"))
self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
"""

