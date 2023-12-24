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
from need.update import *


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
        UpdateWindows()

        # TODO:添加版本更新判断/提示/下载

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
        a = self.is_int(刷屏次数)
        等待秒数 = self.ui.lineEdit_2.text()
        b = self.is_float(等待秒数)
        print(a)
        print(b)
        if not a:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏次数输入错误')
            msg_box.exec_()
        elif not b:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '停顿时间输入错误')
            msg_box.exec_()
        else:
            msg = QMessageBox(QMessageBox.Information, '提示', '刷剪贴板会延时三秒做准备')
            msg.exec_()
            time.sleep(3)
            for __count in range(a):
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                time.sleep(b)
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
            msg_box.exec_()

    def shuaneirong(self):
        刷屏内容 = self.ui.lineEdit_3.text()
        刷屏次数 = self.ui.lineEdit_4.text()
        等待秒数 = self.ui.lineEdit_5.text()
        a = self.is_int(刷屏次数)
        b = self.is_float(等待秒数)
        print(a)
        print(b)
        if not a:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏次数输入错误')
            msg_box.exec_()
        elif not b:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '停顿时间输入错误')
            msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷指定内容会延时三秒做准备')
            msg_box.exec_()
            time.sleep(3)
            pyperclip.copy(刷屏内容)
            for __count in range(a):
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                time.sleep(b)
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
            msg_box.exec_()

    def liandian(self):
        刷屏次数 = int(self.ui.lineEdit_7.text())
        等待秒数 = float(self.ui.lineEdit_8.text())
        a = self.is_int(刷屏次数)
        b = self.is_float(等待秒数)
        print(a)
        print(b)
        if not a:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏次数输入错误')
            msg_box.exec_()
        elif not b:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '停顿时间输入错误')
            msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷表情包会延时五秒做准备')
            msg_box.exec_()
            time.sleep(5)
            for __count in range(a):
                pyautogui.click()
                pyautogui.press('enter')
                time.sleep(b)
            msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
            msg_box.exec_()


class UpdateWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_update()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.show()
        # 创建Thread实例
        t1 = Thread(target=self.getUpdate, args=())
        # 启动线程运行
        t1.start()

    def getUpdate(self):
        try:
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
            self.close()
        except:
            self.ui.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
