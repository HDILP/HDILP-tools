import re
import requests
import os


def getPostPix(url):
    app_name = "HDILP-tools"
    if os.name == 'nt':  # 'nt' ��ʾWindows
        cache_dir = os.path.join(os.getenv('LOCALAPPDATA'), app_name, 'Cache')
    elif os.name == 'posix':  # 'posix' ͨ��ָLinux��macOS
        cache_dir = os.path.join(os.path.expanduser("~"), ".cache", app_name)
    # ȷ��Ŀ¼����
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    # Ȼ������ڴ�Ŀ¼�´�������ȡ��ɾ�������ļ�

    code = requests.get(url).text
    pics = []
    try:
        pictures = (re.findall(r'<img class="fill-img" src="(.*?)">', code))
        for i in pictures:
            i.replace('http', 'https')
            pics.append(i)
        #
        # for i, url in zip(uids, logo_url):  # ����uids��logo_url������ͬ��һһ��Ӧ
        #     response = requests.get(url)
        #     if response.status_code == 200:
        #         file_path = f"./source/avatar/{i}.jpg"
        #         with open(file_path, 'wb') as f:
        #             f.write(response.content)
        #         print(f"ͼƬ�ѳɹ������� {file_path}")
        #     else:
        #         print(f"ΪUID {i} ����ͼƬʧ�ܣ�HTTP״̬�룺{response.status_code}")
        #
        return pics


    except:
        pictures = (re.findall(r"<img src='(.*?)'>", code))
        for i in pictures:
            i.replace('http', 'https')
            pics.append(i)
        return pics
