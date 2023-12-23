import zipfile
import wget
import os


def getUsers():
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
