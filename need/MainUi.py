# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '主页面.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_zhuyemian(object):
    def setupUi(self, MainWindow_zhuyemian):
        MainWindow_zhuyemian.setObjectName("MainWindow_zhuyemian")
        MainWindow_zhuyemian.resize(1436, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow_zhuyemian)
        self.centralwidget.setObjectName("centralwidget")
        self.left = QtWidgets.QLabel(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(40, 20, 340, 490))
        self.left.setStyleSheet("border-image: url(:/resourse/resourse/left.jpg);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;")
        self.left.setText("")
        self.left.setObjectName("left")
        self.right = QtWidgets.QLabel(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(380, 20, 491, 491))
        self.right.setStyleSheet("border-image: url(:/resourse/resourse/right.jpg);\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;")
        self.right.setText("")
        self.right.setObjectName("right")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(480, 160, 284, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("#pushButton{\n"
"    border:none;\n"
"}\n"
"#pushButton:focus{\n"
"    color:rgb(111,111,111);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    border:none;\n"
"}\n"
"#pushButton_2:focus{\n"
"    color:rgb(111,111,111);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"    border:none;\n"
"}\n"
"#pushButton_3:focus{\n"
"    color:rgb(111,111,111);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 70, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(810, 40, 31, 31))
        self.close.setStyleSheet("border-image: url(:/resourse/resourse/close.png);")
        self.close.setText("")
        self.close.setObjectName("close")
        self.minsite = QtWidgets.QPushButton(self.centralwidget)
        self.minsite.setGeometry(QtCore.QRect(770, 40, 31, 31))
        self.minsite.setStyleSheet("border-image: url(:/resourse/resourse/minus.png);")
        self.minsite.setText("")
        self.minsite.setObjectName("minsite")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(390, 210, 471, 291))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.widget_2 = QtWidgets.QWidget(self.page)
        self.widget_2.setGeometry(QtCore.QRect(70, 10, 331, 261))
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 320, 40))
        self.lineEdit.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 85, 320, 40))
        self.lineEdit_2.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 301, 51))
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(0,0,0);\n"
"    border-radius:8px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget_3 = QtWidgets.QWidget(self.page_2)
        self.widget_3.setGeometry(QtCore.QRect(70, 10, 331, 251))
        self.widget_3.setObjectName("widget_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 0, 320, 40))
        self.lineEdit_3.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 60, 320, 40))
        self.lineEdit_4.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(0, 120, 320, 40))
        self.lineEdit_5.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 190, 301, 51))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(0,0,0);\n"
"    border-radius:8px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.widget_4 = QtWidgets.QWidget(self.page_3)
        self.widget_4.setGeometry(QtCore.QRect(70, 10, 331, 251))
        self.widget_4.setObjectName("widget_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(0, 0, 320, 40))
        self.lineEdit_7.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(0, 85, 320, 40))
        self.lineEdit_8.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 190, 301, 51))
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(0,0,0);\n"
"    border-radius:8px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page_3)
        self.right.raise_()
        self.left.raise_()
        self.widget.raise_()
        self.label.raise_()
        self.close.raise_()
        self.minsite.raise_()
        self.stackedWidget.raise_()
        MainWindow_zhuyemian.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_zhuyemian)
        self.stackedWidget.setCurrentIndex(0)
        self.close.clicked.connect(MainWindow_zhuyemian.close)
        self.minsite.clicked.connect(MainWindow_zhuyemian.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_zhuyemian)

    def retranslateUi(self, MainWindow_zhuyemian):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_zhuyemian.setWindowTitle(_translate("MainWindow_zhuyemian", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow_zhuyemian", "刷剪贴板"))
        self.pushButton_2.setText(_translate("MainWindow_zhuyemian", "刷指定内容"))
        self.pushButton_3.setText(_translate("MainWindow_zhuyemian", " 刷表情包（连点）"))
        self.label.setText(_translate("MainWindow_zhuyemian", "刷屏机6.0"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow_zhuyemian", "刷屏次数"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow_zhuyemian", "停顿时间"))
        self.pushButton_4.setText(_translate("MainWindow_zhuyemian", "开始刷屏"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow_zhuyemian", "刷屏内容"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow_zhuyemian", "刷屏次数"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow_zhuyemian", "停顿时间"))
        self.pushButton_5.setText(_translate("MainWindow_zhuyemian", "开始刷屏"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow_zhuyemian", "刷屏次数"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow_zhuyemian", "停顿时间"))
        self.pushButton_6.setText(_translate("MainWindow_zhuyemian", "开始刷屏"))
import need.resourse_rc