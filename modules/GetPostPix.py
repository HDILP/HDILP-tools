import re
import requests
import os


def getPostPix(url):
    app_name = "HDILP-tools"
    if os.name == 'nt':  # 'nt' 表示Windows
        cache_dir = os.path.join(os.getenv('LOCALAPPDATA'), app_name, 'Cache')
    elif os.name == 'posix':  # 'posix' 通常指Linux或macOS
        cache_dir = os.path.join(os.path.expanduser("~"), ".cache", app_name)
    # 确保目录存在
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    # 然后可以在此目录下创建、读取或删除缓存文件

    code = requests.get(url).text
    pics = []
    try:
        pictures = (re.findall(r'<img class="fill-img" src="(.*?)">', code))
        for i in pictures:
            i.replace('http', 'https')
            pics.append(i)
        #
        # for i, url in zip(uids, logo_url):  # 假设uids和logo_url长度相同，一一对应
        #     response = requests.get(url)
        #     if response.status_code == 200:
        #         file_path = f"./source/avatar/{i}.jpg"
        #         with open(file_path, 'wb') as f:
        #             f.write(response.content)
        #         print(f"图片已成功保存至 {file_path}")
        #     else:
        #         print(f"为UID {i} 下载图片失败，HTTP状态码：{response.status_code}")
        #
        return pics


    except:
        pictures = (re.findall(r"<img src='(.*?)'>", code))
        for i in pictures:
            i.replace('http', 'https')
            pics.append(i)
        return pics
