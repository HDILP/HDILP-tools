from concurrent.futures import ThreadPoolExecutor
import sys
import time
import pyperclip
import pyautogui
# import os
# import wget
# import zipfile

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
# from threading import Thread
from need.NewMainUI import *


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)

        self.ui.home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.shuapingqi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        self.ui.pushButton_1.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.pushButton_4.clicked.connect(self.shuajiantieban_thread)
        self.ui.pushButton_5.clicked.connect(self.shuaneirong_thread)
        self.ui.pushButton_6.clicked.connect(self.liandian_thread)
        self.show()
        # msg_box = QMessageBox(QMessageBox.Information, '提示', '刷剪贴板请提前复制刷屏内容')
        # msg_box.exec_()
        # TODO：把提示写进UI里

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def is_float(self, var):
        try:
            float(var)
            return True
        except (ValueError, TypeError):
            return False

    def is_int(self, var):
        try:
            int(var)
            return True
        except (ValueError, TypeError):
            return False

    def shuajiantieban(self):
        刷屏次数 = self.ui.lineEdit.text()
        等待秒数 = self.ui.lineEdit_2.text()
        a = int(刷屏次数)
        b = float(等待秒数)
        time.sleep(3)
        for __count in range(a):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(b)

    def shuajiantieban_thread(self):
        thread = self.ui.spinBox.value()
        a = self.is_int(self.ui.lineEdit.text())  # 刷屏次数
        b = self.is_float(self.ui.lineEdit_2.text())  # 等待秒数
        if not a:  # 假
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏次数输入错误')
            msg_box.exec_()
        elif not b:  # 假
            msg_box = QMessageBox(QMessageBox.Information, '提示', '停顿时间输入错误')
            msg_box.exec_()
        else:  # 真
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷剪贴板会延时三秒做准备')
            msg_box.exec_()
            with ThreadPoolExecutor(max_workers=thread) as pool:
                for i in range(1, thread + 1):
                    pool.submit(self.shuajiantieban)
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
            msg_box.exec_()
            #  TODO:把消息框做成一个函数

    def shuaneirong(self):
        刷屏内容 = self.ui.lineEdit_3.text()
        刷屏次数 = self.ui.lineEdit_4.text()
        等待秒数 = self.ui.lineEdit_5.text()
        a = int(刷屏次数)
        b = float(等待秒数)
        time.sleep(3)
        pyperclip.copy(刷屏内容)
        for __count in range(a):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(b)

    def shuaneirong_thread(self):
        thread = self.ui.spinBox.value()
        a = self.is_int(self.ui.lineEdit_4.text())  # 刷屏次数
        b = self.is_float(self.ui.lineEdit_5.text())  # 等待秒数
        if not a:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏次数输入错误')
            msg_box.exec_()
        elif not b:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '停顿时间输入错误')
            msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷指定内容会延时三秒做准备')
            msg_box.exec_()
            with ThreadPoolExecutor(max_workers=thread) as pool:
                for i in range(1, thread + 1):
                    pool.submit(self.shuaneirong)
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
            msg_box.exec_()


    def liandian(self):
        刷屏次数 = self.ui.lineEdit_7.text()
        等待秒数 = self.ui.lineEdit_8.text()
        a = int(刷屏次数)
        b = float(等待秒数)
        print(a)
        print(b)
        time.sleep(5)
        for __count in range(a):
            pyautogui.click()
            pyautogui.press('enter')
            time.sleep(b)

    def liandian_thread(self):
        thread = self.ui.spinBox.value()
        a = self.is_int(self.ui.lineEdit_7.text())  # 刷屏次数
        b = self.is_float(self.ui.lineEdit_8.text())  # 等待秒数
        if not a:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏次数输入错误')
            msg_box.exec_()
        elif not b:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '停顿时间输入错误')
            msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷表情包会延时五秒做准备')
            msg_box.exec_()
            with ThreadPoolExecutor(max_workers=thread) as pool:
                for i in range(1, thread + 1):
                    pool.submit(self.liandian)
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
            msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    sys.exit(app.exec_())
