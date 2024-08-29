import sys, os, shutil

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from need.NewMainUI import *

import modules.rollscreen
import modules.AntiBanWord
import modules.GetPostPix


class MainUi(QMainWindow, QApplication):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initUI()
        modules.GetPostPix.mkCacheDir()  # 创建缓存文件夹
        
        self.show()
    
    def initUI(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 去掉标题栏
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

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
        self.ui.antibanword.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(0))
        self.ui.getpostpicture.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(1))
        self.ui.conversion.clicked.connect(self.var_to_AntiBanWord)
        self.ui.Download_pics.clicked.connect(self.get_post_pictures)
        self.ui.Save_pics.clicked.connect(self.save_pictures)

    @pyqtSlot()
    def on_about_to_quit(self):
        # 在应用程序即将退出时执行清理工作
        modules.GetPostPix.cleanUp()
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

    # ========== anti ban word ==========
    def var_to_AntiBanWord(self):
        before_conversion_word = self.ui.plainTextEdit.toPlainText()
        print(before_conversion_word)
        after_conversion_text = modules.AntiBanWord.conversion(before_conversion_word)
        self.ui.plainTextEdit_2.setPlainText(after_conversion_text)

    # ======== get post picture =========
    def get_post_pictures(self):
        post_url = self.ui.plainTextEdit_3.toPlainText()  # 获取输入文章链接
        self.pics_path = modules.GetPostPix.getPostPix(post_url)
        
        self.ui.Save_pics.setEnabled(True)
            
        for i, path in enumerate(self.pics_path, start=1): # type: ignore
            pic = QPixmap(path).scaled(70, 100, Qt.KeepAspectRatio)
            # 更新对应的图片控件
            # 直接使用getattr来获取对应的图片控件
            pic_control = getattr(self.ui, f"pic_{i}", None)
            checker_control = getattr(self.ui, f"checkBox_{i}", None)
            
            if pic_control is not None and checker_control is not None:
                pic_control.setPixmap(pic)
                checker_control.setCheckable(True)
                self.ui.Save_pics.setEnabled(True)

    def save_pictures(self):
        save_path = QFileDialog.getExistingDirectory(self,
                                                    "选择存放图片的文件夹",
                                                    os.getcwd())
        # 避免 TypeError
        if not isinstance(self.pics_path, list):
            print("pics_path 不是列表类型")
            return
        
        try:
            # 避免 IndexError
            for i in range(len(self.pics_path)):
                checker_control = getattr(self.ui, f"checkBox_{i + 1}", None)
                if checker_control is not None and checker_control.isChecked():
                    modules.GetPostPix.copyPix(self.pics_path[i], save_path)
                    print(f"图片 {i + 1} 已保存到 {save_path}")
                    msg_box = QMessageBox(QMessageBox.Information, '提示', f"图片 {i + 1} 已保存到 {save_path}")
                    msg_box.exec_()
        except IndexError:
            print("列表索引越界")
        except Exception as e:
            print(f"保存图片时发生错误: {e}")
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    app.aboutToQuit.connect(win.on_about_to_quit)
    sys.exit(app.exec_())
