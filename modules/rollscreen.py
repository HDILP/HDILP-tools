import time
from pyperclip import copy
from pyautogui import hotkey, press, click
from PyQt5.QtWidgets import QMessageBox
from concurrent.futures import ThreadPoolExecutor


def is_float(var):
    try:
        float(var)
        return True
    except (ValueError, TypeError):
        return False


def is_int(var):
    try:
        int(var)
        return True
    except (ValueError, TypeError):
        return False


def shuajiantieban_thread(thread, roll_num, delay_num):
    a = is_int(roll_num)  # 刷屏次数
    b = is_float(delay_num)  # 等待秒数
    if not a:  # 假
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏次数输入错误')
        msg_box.exec_()
    elif not b:  # 假
        msg_box = QMessageBox(QMessageBox.Information, '提示', '停顿时间输入错误')
        msg_box.exec_()
    else:  # 真
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷剪贴板会延时三秒做准备')
        msg_box.exec_()
        a = int(roll_num)
        b = float(delay_num)

        def shuajiantieban():
            time.sleep(3)
            for __count in range(a):
                hotkey('ctrl', 'v')
                press('enter')
                time.sleep(b)

        with ThreadPoolExecutor(max_workers=thread) as pool:
            for i in range(1, thread + 1):
                pool.submit(shuajiantieban)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
        msg_box.exec_()
        #  TODO:把消息框做成一个函数


def shuaneirong_thread(thread, text, roll_num, delay_num):
    a = is_int(roll_num)  # 刷屏次数
    b = is_float(delay_num)  # 等待秒数
    if not a:
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏次数输入错误')
        msg_box.exec_()
    elif not b:
        msg_box = QMessageBox(QMessageBox.Information, '提示', '停顿时间输入错误')
        msg_box.exec_()
    else:
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷指定内容会延时三秒做准备')
        msg_box.exec_()
        a = int(roll_num)
        b = float(delay_num)

        def shuaneirong():
            time.sleep(3)
            copy(text)
            for __count in range(a):
                hotkey('ctrl', 'v')
                press('enter')
                time.sleep(b)

        with ThreadPoolExecutor(max_workers=thread) as pool:
            for i in range(1, thread + 1):
                pool.submit(shuaneirong)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
        msg_box.exec_()


def liandian_thread(thread, roll_num, delay_num):
    a = is_int(roll_num)  # 刷屏次数
    b = is_float(delay_num)  # 等待秒数
    if not a:
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏次数输入错误')
        msg_box.exec_()
    elif not b:
        msg_box = QMessageBox(QMessageBox.Information, '提示', '停顿时间输入错误')
        msg_box.exec_()
    else:
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷表情包会延时五秒做准备')
        msg_box.exec_()
        a = int(roll_num)
        b = float(delay_num)

        def liandian():
            time.sleep(5)
            for __count in range(a):
                click()
                press('enter')
                time.sleep(b)

        with ThreadPoolExecutor(max_workers=thread) as pool:
            for i in range(1, thread + 1):
                pool.submit(liandian)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
        msg_box.exec_()
