import time
import pyperclip
import pyautogui
from PyQt5.QtWidgets import QMessageBox
from concurrent.futures import ThreadPoolExecutor

import index_new


def shuajiantieban(roll_num, delay_num):
    a = int(roll_num)
    b = float(delay_num)
    time.sleep(3)
    for __count in range(a):
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(b)


def shuaneirong(text, roll_num, delay_num):
    a = int(roll_num)
    b = float(delay_num)
    time.sleep(3)
    pyperclip.copy(text)
    for __count in range(a):
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(b)


def liandian(roll_num, delay_num):
    a = int(roll_num)
    b = float(delay_num)
    time.sleep(5)
    for __count in range(a):
        pyautogui.click()
        pyautogui.press('enter')
        time.sleep(b)


def shuajiantieban_thread(thread, roll_num, delay_num):
    a = index_new.is_int(roll_num)  # 刷屏次数
    b = index_new.is_float(delay_num)  # 等待秒数
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
                pool.submit(shuajiantieban, roll_num, delay_num)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
        msg_box.exec_()
        #  TODO:把消息框做成一个函数


def shuaneirong_thread(thread, text, roll_num, delay_num):
    a = index_new.is_int(roll_num)  # 刷屏次数
    b = index_new.is_float(delay_num)  # 等待秒数
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
                pool.submit(shuaneirong, text, roll_num, delay_num)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
        msg_box.exec_()


def liandian_thread(thread, roll_num, delay_num):
    a = index_new.is_int(roll_num)  # 刷屏次数
    b = index_new.is_float(delay_num)  # 等待秒数
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
                pool.submit(liandian, roll_num, delay_num)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '刷屏完成')
        msg_box.exec_()
