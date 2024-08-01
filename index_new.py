import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from need.NewMainUI import *

import modules.rollscreen
import modules.AntiBanWord


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.stackedWidget_3.setCurrentIndex(0)

        self.ui.home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        self.ui.shuapingqi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_1.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.pushButton_4.clicked.connect(self.var_to_shuajiantieban)
        self.ui.pushButton_5.clicked.connect(self.var_to_shuaneirong)
        self.ui.pushButton_6.clicked.connect(self.var_to_liandian)

        self.ui.fkst_tools.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.conversion.clicked.connect(self.var_to_AntiBanWord)

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

    # =========== roll screen ===========
    def var_to_shuajiantieban(self):
        thread_num = self.ui.spinBox.value()
        roll_num = self.ui.lineEdit.text()
        delay_num = self.ui.lineEdit_2.text()
        modules.rollscreen.liandian_thread(thread_num, roll_num, delay_num)

    def var_to_shuaneirong(self):
        thread_num = self.ui.spinBox.value()
        text = self.ui.lineEdit_3.text()
        roll_num = self.ui.lineEdit_4.text()
        delay_num = self.ui.lineEdit_5.text()
        modules.rollscreen.shuaneirong_thread(thread_num, text, roll_num, delay_num)

    def var_to_liandian(self):
        thread_num = self.ui.spinBox.value()
        roll_num = self.ui.lineEdit_7.text()
        delay_num = self.ui.lineEdit_8.text()
        modules.rollscreen.liandian_thread(thread_num, roll_num, delay_num)

    # ===================================

    # ========== anti ban word ==========
    def var_to_AntiBanWord(self):
        before_conversion_word = self.ui.plainTextEdit.toPlainText()
        print(before_conversion_word)
        after_conversion_text = modules.AntiBanWord.conversion(before_conversion_word)
        self.ui.plainTextEdit_2.setPlainText(after_conversion_text)

    # ===================================


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    sys.exit(app.exec_())
