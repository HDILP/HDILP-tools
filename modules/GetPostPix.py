# coding=utf-8
import re
import requests
import os
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import shutil

cache_dir = ''

def mkCacheDir():
    app_name = "HDILP-tools"
    global cache_dir
    if os.name == 'nt':  # 'nt' 表示Windows
        cache_dir = os.path.join(os.environ['tmp'], app_name)
    elif os.name == 'posix':  # 'posix' 通常指Linux或macOS
        cache_dir = os.path.join(os.path.expanduser("~"), ".cache", app_name)
    # 确保目录存在
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    # 然后可以在此目录下创建、读取或删除缓存文件

def getPostPix(url: str):
    try:
        code = requests.get(url).text

    except requests.exceptions.MissingSchema:
        msg_box = QMessageBox(QMessageBox.Information, '提示', '文章链接输入错误')
        msg_box.exec_()
        return

    else:     
        try:
            pictures = (re.findall(r'<img class="fill-img" src="(.*?)">', code))
            return getPix(pictures)
        
        except:
            pictures = (re.findall(r"<img src='(.*?)'>", code))
            return getPix(pictures)


def getPix(pictures):
    if len(pictures) == 0:
        msg_box = QMessageBox(QMessageBox.Information, '提示', '文章内无图片')
        msg_box.exec_()
        return
    
    pics_url: list[str] = []
    locale_path: list[str] = []
    for i in pictures:
        i.replace('http', 'https')
        pics_url.append(i)

    for url in pics_url:
        response = requests.get(url)
        if response.status_code == 200:
            name = re.findall(r"/../../(.*?)\.", url)[0]
            file_path = os.path.join(cache_dir, f"{name}.jpg")
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(url)
            print(f"图片已成功保存至 {file_path}")
            locale_path.append(file_path)
        else:
            print(f"为UID {i} 下载图片失败，HTTP状态码：{response.status_code}")
    
    return locale_path
def copyPix(path1: str, path2: str):
    shutil.copy(path1, path2)

def cleanUp():
    shutil.rmtree(cache_dir)
    print(cache_dir)
    print("缓存目录已清空")