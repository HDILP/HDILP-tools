import sys
import time
import pyperclip
import pyautogui
import os
import wget
import zipfile

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from threading import Thread
from need.LoginUI import *
from need.MainUi import *


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(self.go_to_inter)
        self.ui.pushButton_1.clicked.connect(self.register)
        self.show()
        # 创建两个Thread实例
        t1 = Thread(target=self.getUsers, args=())
        # 启动线程运行
        t1.start()
        # TODO:添加更新判断/提示/下载

    def getUsers(self):
        url = 'https://hdilp.top/users.zip'
        out = 'C:/Windows/Temp/'
        name = wget.download(url, out)
        print(name)
        # 读取压缩文件
        file = zipfile.ZipFile(name)
        # 解压文件
        print('开始解压...')
        file.extractall(out)
        print('解压结束。')
        # 关闭文件流
        file.close()
        os.remove(name)
        # TODO：添加更新提示/进度条

    def register(self):
        msg_box = QMessageBox(QMessageBox.Information, '提示', '请联系作者')
        msg_box.exec_()

    def go_to_inter(self):
        account = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        out = 'C:/Windows/Temp'
        user_list = os.listdir(out + '/users')  # 遍历元组，判断user_id是否在元组中
        flag = 0
        for user in user_list:
            if user == account:
                print('登录中····')
                # 打开文件
                file_name = out + '/users/' + account
                file_user = open(file_name)
                # 获取文件内容
                user_info = eval(file_user.read())
                if password == user_info['u_pwd']:
                    # if account == "HDILP" and password == "":
                    flag = 1
                    self.close()
                    zhuyemian()

        if flag != 1:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '账号或密码错误')
            msg_box.exec_()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


class zhuyemian(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_zhuyemian()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_4.clicked.connect(self.shuajiantieban)
        self.ui.pushButton_5.clicked.connect(self.shuaneirong)
        self.ui.pushButton_6.clicked.connect(self.liandian)
        self.show()
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷剪贴板请提前复制刷屏内容')
        msg_box.exec_()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def shuajiantieban(self):
        刷屏次数 = int(self.ui.lineEdit.text())
        等待秒数 = float(self.ui.lineEdit_2.text())
        # TODO：判断变量是否为数字
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷剪贴板会延时三秒做准备')
        msg_box.exec_()
        time.sleep(3)
        for __count in range(刷屏次数):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(等待秒数)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
        msg_box.exec_()

    def shuaneirong(self):
        刷屏内容 = self.ui.lineEdit_3.text()
        刷屏次数 = int(self.ui.lineEdit_4.text())
        等待秒数 = float(self.ui.lineEdit_5.text())
        # TODO：判断变量是否为数字
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷指定内容会延时三秒做准备')
        msg_box.exec_()
        time.sleep(3)
        pyperclip.copy(刷屏内容)
        for __count in range(刷屏次数):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(等待秒数)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
        msg_box.exec_()

    def liandian(self):
        刷屏次数 = int(self.ui.lineEdit_7.text())
        等待秒数 = float(self.ui.lineEdit_8.text())
        # TODO：判断变量是否为数字
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷表情包会延时五秒做准备')
        msg_box.exec_()
        time.sleep(5)
        for __count in range(刷屏次数):
            pyautogui.click()
            pyautogui.press('enter')
            time.sleep(等待秒数)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
