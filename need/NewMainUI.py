# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewMainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 960, 540))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(92, 170, 255, 255), stop:1 rgba(255, 170, 255, 255));\n"
"\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 980, 560))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,30);\n"
"\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 960, 70))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255,40);\n"
"border-top-left-radius:20px;\n"
"\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 80, 960, 3))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("QProgressBar { border: 2px; border-radius: 5px; background-color: #b3e5fc; text-align: center;}\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #b3e5fc, stop:1 rgb(255, 184, 210));\n"
"\n"
"}")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 140, 470))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255,50);\n"
"border-bottom-left-radius:20px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(20, 110, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        font.setPointSize(14)
        font.setItalic(False)
        font.setKerning(False)
        self.home.setFont(font)
        self.home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.home.setStyleSheet("background-color: rgba(255, 255, 255,50);\n"
"border:1px solid rgba(255, 170, 255, 75);\n"
"border-radius:8px;\n"
"text-align:left")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/home_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon)
        self.home.setIconSize(QtCore.QSize(36, 36))
        self.home.setCheckable(False)
        self.home.setObjectName("home")
        self.shuapingqi = QtWidgets.QPushButton(self.centralwidget)
        self.shuapingqi.setGeometry(QtCore.QRect(20, 170, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shuapingqi.sizePolicy().hasHeightForWidth())
        self.shuapingqi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        font.setPointSize(14)
        font.setItalic(False)
        font.setKerning(False)
        self.shuapingqi.setFont(font)
        self.shuapingqi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shuapingqi.setStyleSheet("background-color: rgba(255, 255, 255,50);\n"
"border:1px solid rgba(255, 170, 255, 75);\n"
"border-radius:8px;\n"
"text-align:left")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/sort_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuapingqi.setIcon(icon1)
        self.shuapingqi.setIconSize(QtCore.QSize(36, 36))
        self.shuapingqi.setCheckable(False)
        self.shuapingqi.setObjectName("shuapingqi")
        self.min = QtWidgets.QPushButton(self.centralwidget)
        self.min.setGeometry(QtCore.QRect(880, 30, 24, 24))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.min.setFont(font)
        self.min.setStyleSheet("border-image: url(:/icons/icons/remove_FILL0_wght400_GRAD0_opsz24.png);")
        self.min.setText("")
        self.min.setObjectName("min")
        self.close_2 = QtWidgets.QPushButton(self.centralwidget)
        self.close_2.setGeometry(QtCore.QRect(920, 30, 24, 24))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.close_2.setFont(font)
        self.close_2.setStyleSheet("border-image: url(:/icons/icons/close_FILL0_wght400_GRAD0_opsz24.png);")
        self.close_2.setText("")
        self.close_2.setObjectName("close_2")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 25, 141, 41))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(150, 80, 821, 471))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(100, 80, 600, 250))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 141, 471))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.widget_2.setFont(font)
        self.widget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 255,50);\n"
"border:1px;\n"
"border-radius:8px;")
        self.widget_2.setObjectName("widget_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 30, 101, 30))
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"background-color: rgba(255, 255, 255,75);\n"
"border-radius:6px;\n"
"\n"
"}\n"
"#pushButton_3:focus{\n"
"    color:rgb(111,111,111);\n"
"}")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_1 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 130, 100, 30))
        self.pushButton_1.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.pushButton_1.setFont(font)
        self.pushButton_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_1.setStyleSheet("#pushButton_1{\n"
"background-color: rgba(255, 255, 255,75);\n"
"border-radius:6px;\n"
"\n"
"}\n"
"#pushButton_1:focus{\n"
"    color:rgb(111,111,111);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 100, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    background-color: rgba(255, 255, 255,75);\n"
"    border-radius:6px;\n"
"\n"
"}\n"
"#pushButton_2:focus{\n"
"    color:rgb(111,111,111);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_2)
        self.stackedWidget_2.setGeometry(QtCore.QRect(210, 100, 471, 321))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.stackedWidget_2.setFont(font)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.widget_3 = QtWidgets.QWidget(self.page_3)
        self.widget_3.setGeometry(QtCore.QRect(70, 10, 321, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 320, 40))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("\n"
"border-radius:8px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 85, 320, 40))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("\n"
"border-radius:8px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 301, 51))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.widget_4 = QtWidgets.QWidget(self.page_4)
        self.widget_4.setGeometry(QtCore.QRect(70, 10, 321, 251))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.widget_4.setFont(font)
        self.widget_4.setObjectName("widget_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 0, 320, 40))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("\n"
"border-radius:8px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 60, 320, 40))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("\n"
"border-radius:8px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(0, 120, 320, 40))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("\n"
"border-radius:8px")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 190, 301, 51))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.widget_5 = QtWidgets.QWidget(self.page_5)
        self.widget_5.setGeometry(QtCore.QRect(70, 10, 321, 251))
        self.widget_5.setObjectName("widget_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(0, 0, 320, 40))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("\n"
"border-radius:8px")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(0, 85, 320, 40))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("\n"
"border-radius:8px")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 190, 301, 51))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget_2.addWidget(self.page_5)
        self.spinBox = QtWidgets.QSpinBox(self.page_2)
        self.spinBox.setGeometry(QtCore.QRect(740, 420, 51, 22))
        self.spinBox.setStyleSheet("QSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 4px;\n"
"    padding-right: 15px;\n"
"    border: 1px solid rgb(235,235,235);\n"
"    border-radius: 3px;\n"
"    /*color: rgb(200,200,200);*/\n"
"    background-color: rgb(235,235,235);\n"
"    selection-color: rgb(235,235,235);\n"
"    selection-background-color: rgb(235,235,235);\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"\n"
"")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(64)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(673, 420, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.progressBar_2 = QtWidgets.QProgressBar(self.page_2)
        self.progressBar_2.setGeometry(QtCore.QRect(0, 4, 1, 466))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.progressBar_2.setFont(font)
        self.progressBar_2.setToolTipDuration(-1)
        self.progressBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_2.setStyleSheet("QProgressBar { border: 2px; border-radius: 5px; background-color: #b3e5fc; text-align: center;}\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #b3e5fc, stop:1 rgb(255, 184, 210));\n"
"\n"
"}")
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(1)
        self.progressBar_2.setProperty("value", 1)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setFormat("")
        self.progressBar_2.setObjectName("progressBar_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.progressBar_3 = QtWidgets.QProgressBar(self.page_6)
        self.progressBar_3.setGeometry(QtCore.QRect(0, 0, 1, 466))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.progressBar_3.setFont(font)
        self.progressBar_3.setToolTipDuration(-1)
        self.progressBar_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_3.setStyleSheet("QProgressBar { border: 2px; border-radius: 5px; background-color: #b3e5fc; text-align: center;}\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #b3e5fc, stop:1 rgb(255, 184, 210));\n"
"\n"
"}")
        self.progressBar_3.setMinimum(0)
        self.progressBar_3.setMaximum(1)
        self.progressBar_3.setProperty("value", 1)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setInvertedAppearance(False)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_3.setFormat("")
        self.progressBar_3.setObjectName("progressBar_3")
        self.widget_6 = QtWidgets.QWidget(self.page_6)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 141, 471))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.widget_6.setFont(font)
        self.widget_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_6.setAutoFillBackground(False)
        self.widget_6.setStyleSheet("background-color: rgba(255, 255, 255,50);\n"
"border:1px;\n"
"border-radius:8px;")
        self.widget_6.setObjectName("widget_6")
        self.antibanword = QtWidgets.QPushButton(self.widget_6)
        self.antibanword.setEnabled(True)
        self.antibanword.setGeometry(QtCore.QRect(20, 30, 101, 30))
        self.antibanword.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.antibanword.setFont(font)
        self.antibanword.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.antibanword.setStyleSheet("#antibanword{\n"
"background-color: rgba(255, 255, 255,75);\n"
"border-radius:6px;\n"
"}\n"
"#antibanword:focus{\n"
"    color:rgb(111,111,111);\n"
"}")
        self.antibanword.setAutoDefault(False)
        self.antibanword.setObjectName("antibanword")
        self.getpostpicture = QtWidgets.QPushButton(self.widget_6)
        self.getpostpicture.setEnabled(True)
        self.getpostpicture.setGeometry(QtCore.QRect(20, 80, 101, 30))
        self.getpostpicture.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.getpostpicture.setFont(font)
        self.getpostpicture.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.getpostpicture.setStyleSheet("#getpostpicture{\n"
"background-color: rgba(255, 255, 255,75);\n"
"border-radius:6px;\n"
"}\n"
"#getpostpicture:focus{\n"
"    color:rgb(111,111,111);\n"
"}")
        self.getpostpicture.setAutoDefault(False)
        self.getpostpicture.setObjectName("getpostpicture")
        self.widget_7 = QtWidgets.QWidget(self.page_6)
        self.widget_7.setGeometry(QtCore.QRect(140, 0, 671, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.widget_7)
        self.stackedWidget_3.setGeometry(QtCore.QRect(10, 10, 661, 451))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.conversion = QtWidgets.QPushButton(self.page_7)
        self.conversion.setGeometry(QtCore.QRect(170, 410, 301, 51))
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.conversion.setFont(font)
        self.conversion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.conversion.setObjectName("conversion")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.page_7)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(340, 10, 320, 390))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 10px; /* 您可以根据需要调整圆角的大小 */\n"
"    background-color: rgba(255, 255, 255, 1); /* 示例：白色背景，可按需修改 */\n"
"    padding: 5px; /* 文本与边框的间距，可选 */\n"
"}\n"
"")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page_7)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 320, 390))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEdit.setStyleSheet("\n"
"QPlainTextEdit {\n"
"    border-radius: 10px; /* 您可以根据需要调整圆角的大小 */\n"
"    background-color: rgba(255, 255, 255, 1); /* 示例：白色背景，可按需修改 */\n"
"    padding: 5px; /* 文本与边框的间距，可选 */\n"
"}\n"
"")
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.stackedWidget_3.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.page_8)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(30, 30, 601, 91))
        self.plainTextEdit_3.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 10px; /* 您可以根据需要调整圆角的大小 */\n"
"    background-color: rgba(255, 255, 255, 1); /* 示例：白色背景，可按需修改 */\n"
"    padding: 5px; /* 文本与边框的间距，可选 */\n"
"}")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.pic = QtWidgets.QLabel(self.page_8)
        self.pic.setGeometry(QtCore.QRect(0, 130, 75, 100))
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
        self.pic.setObjectName("pic")
        self.pic_2 = QtWidgets.QLabel(self.page_8)
        self.pic_2.setGeometry(QtCore.QRect(80, 130, 75, 100))
        self.pic_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_2.setObjectName("pic_2")
        self.pic_3 = QtWidgets.QLabel(self.page_8)
        self.pic_3.setGeometry(QtCore.QRect(160, 130, 75, 100))
        self.pic_3.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_3.setObjectName("pic_3")
        self.pic_4 = QtWidgets.QLabel(self.page_8)
        self.pic_4.setGeometry(QtCore.QRect(240, 130, 75, 100))
        self.pic_4.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_4.setObjectName("pic_4")
        self.pic_5 = QtWidgets.QLabel(self.page_8)
        self.pic_5.setGeometry(QtCore.QRect(320, 130, 75, 100))
        self.pic_5.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_5.setObjectName("pic_5")
        self.pic_6 = QtWidgets.QLabel(self.page_8)
        self.pic_6.setGeometry(QtCore.QRect(400, 130, 75, 100))
        self.pic_6.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_6.setObjectName("pic_6")
        self.pic_7 = QtWidgets.QLabel(self.page_8)
        self.pic_7.setGeometry(QtCore.QRect(480, 130, 75, 100))
        self.pic_7.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_7.setObjectName("pic_7")
        self.pic_8 = QtWidgets.QLabel(self.page_8)
        self.pic_8.setGeometry(QtCore.QRect(560, 130, 75, 100))
        self.pic_8.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_8.setObjectName("pic_8")
        self.pic_9 = QtWidgets.QLabel(self.page_8)
        self.pic_9.setGeometry(QtCore.QRect(0, 260, 75, 100))
        self.pic_9.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_9.setObjectName("pic_9")
        self.checkBox = QtWidgets.QCheckBox(self.page_8)
        self.checkBox.setGeometry(QtCore.QRect(30, 230, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setText("")
        self.checkBox.setCheckable(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.page_8)
        self.checkBox_2.setGeometry(QtCore.QRect(110, 230, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_8)
        self.checkBox_3.setGeometry(QtCore.QRect(190, 230, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.page_8)
        self.checkBox_4.setGeometry(QtCore.QRect(270, 230, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.page_8)
        self.checkBox_5.setGeometry(QtCore.QRect(350, 230, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.page_8)
        self.checkBox_6.setGeometry(QtCore.QRect(430, 230, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.page_8)
        self.checkBox_7.setGeometry(QtCore.QRect(510, 230, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy)
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.page_8)
        self.checkBox_8.setGeometry(QtCore.QRect(590, 230, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy)
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.page_8)
        self.checkBox_9.setGeometry(QtCore.QRect(30, 360, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy)
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.Download_pics = QtWidgets.QPushButton(self.page_8)
        self.Download_pics.setGeometry(QtCore.QRect(240, 380, 150, 50))
        self.Download_pics.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.Download_pics.setObjectName("Download_pics")
        self.stackedWidget_3.addWidget(self.page_8)
        self.stackedWidget.addWidget(self.page_6)
        self.fkst_tools = QtWidgets.QPushButton(self.centralwidget)
        self.fkst_tools.setGeometry(QtCore.QRect(20, 230, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fkst_tools.sizePolicy().hasHeightForWidth())
        self.fkst_tools.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("OPlusSans 3.0")
        font.setPointSize(14)
        font.setItalic(False)
        font.setKerning(False)
        self.fkst_tools.setFont(font)
        self.fkst_tools.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fkst_tools.setStyleSheet("background-color: rgba(255, 255, 255,50);\n"
"border:1px solid rgba(255, 170, 255, 75);\n"
"border-radius:8px;\n"
"text-align:left")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/fkst.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fkst_tools.setIcon(icon2)
        self.fkst_tools.setIconSize(QtCore.QSize(36, 36))
        self.fkst_tools.setCheckable(False)
        self.fkst_tools.setObjectName("fkst_tools")
        self.label_2.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.progressBar.raise_()
        self.label_3.raise_()
        self.home.raise_()
        self.shuapingqi.raise_()
        self.min.raise_()
        self.close_2.raise_()
        self.title.raise_()
        self.stackedWidget.raise_()
        self.fkst_tools.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.min.clicked.connect(MainWindow.showMinimized)
        self.close_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home.setText(_translate("MainWindow", "主页"))
        self.shuapingqi.setText(_translate("MainWindow", "刷屏器"))
        self.title.setText(_translate("MainWindow", "寒澈工具箱"))
        self.stackedWidget.setStatusTip(_translate("MainWindow", "线程数"))
        self.label_5.setText(_translate("MainWindow", "Welcome!\n"
"\n"
"欢迎使用寒澈工具箱(*^▽^*)\n"
"请在左边的工具栏选择你需要的工具。"))
        self.pushButton_3.setText(_translate("MainWindow", " 刷表情包（连点）"))
        self.pushButton_1.setText(_translate("MainWindow", "刷剪贴板"))
        self.pushButton_2.setText(_translate("MainWindow", "刷指定内容"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "刷屏次数"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "停顿时间"))
        self.pushButton_4.setText(_translate("MainWindow", "开始刷屏"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "刷屏内容"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "刷屏次数"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "停顿时间"))
        self.pushButton_5.setText(_translate("MainWindow", "开始刷屏"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "刷屏次数"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "停顿时间"))
        self.pushButton_6.setText(_translate("MainWindow", "开始刷屏"))
        self.spinBox.setWhatsThis(_translate("MainWindow", "线程数"))
        self.label_6.setText(_translate("MainWindow", "线程数："))
        self.antibanword.setText(_translate("MainWindow", "反屏蔽词"))
        self.getpostpicture.setText(_translate("MainWindow", "提取文章图片"))
        self.conversion.setText(_translate("MainWindow", "转换"))
        self.plainTextEdit_2.setPlaceholderText(_translate("MainWindow", "转换后文本"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "转换前文本"))
        self.plainTextEdit_3.setPlaceholderText(_translate("MainWindow", "请输入文章分享链接"))
        self.pic.setText(_translate("MainWindow", "1"))
        self.pic_2.setText(_translate("MainWindow", "2"))
        self.pic_3.setText(_translate("MainWindow", "3"))
        self.pic_4.setText(_translate("MainWindow", "4"))
        self.pic_5.setText(_translate("MainWindow", "5"))
        self.pic_6.setText(_translate("MainWindow", "6"))
        self.pic_7.setText(_translate("MainWindow", "7"))
        self.pic_8.setText(_translate("MainWindow", "8"))
        self.pic_9.setText(_translate("MainWindow", "9"))
        self.Download_pics.setText(_translate("MainWindow", "下载"))
        self.fkst_tools.setText(_translate("MainWindow", "疯狂刷题"))
import need.NewRes_rc
