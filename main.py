import threading
import time

import requests
from bs4 import BeautifulSoup

import urllib.request

def getPic():

    res = requests.get("https://cn.bing.com/images/search?q=%E5%9B%BE%E7%89%87&qpvt=%e5%9b%be%e7%89%87&form=IGRE&first=1&cw=1302&ch=966")

    html  = res.text

    soup = BeautifulSoup(html,'html.parser')

    imgs = soup.find_all("img")
    i = 0
    for img in imgs:

        imgsrc = img.get("src")
        print(imgsrc)
        if imgsrc is not None and imgsrc.startswith("https"):
            urllib.request.urlretrieve(img.get("src"), "D:/files/picture%d.jpg"%i)
            print(f"正在下载第{i}张图片")
            i = i+1


def login(url, data, headers):
    r = s.post(url=url, json=data, headers=headers)
    print(r.text)


if __name__ == '__main__':

    # 个人私聊
    url = 'https://staging-meet-api.miyachat.com/auth/SendSmsCodeForLogin'
    data = {
        "mobile": "86-15919666772",
        "validate": ""

    }
    print(data)
    s = requests.session()

    headers = {

        "Referer": "https://staging-meecnh5hre8z7dnmr6ww8ka5sd4xwt.miyachat.com/",
        "Content-Type": "application/json;charset=UTF-8"
    }
    threads = []
    for i in range(100):
        login(url,data,headers)
        time.sleep(0.1)
        thread= threading.Thread(target=login, args=(url,data,headers,))
        threads.append(thread)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

