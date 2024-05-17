import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

phone = "13546800908"

token = "x4fs3am17f8ujdmxsppegqjww"

def getCookie():
    driver = webdriver.Edge()
    path = f"https://staging-meet.miyachat.com/login"
    driver.get(path)

    input = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[2]/div/span/form/div[1]/span/div[2]/input")
    input.click()
    input.send_keys(phone)

    getCode = driver.find_element(By.CLASS_NAME,"login-mobile-btn")
    getCode.click()
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[1]/div[2]/div/span/form/div[2]/span/div/input").click()
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'search-box__input'))
    )

    token = driver.get_cookie("token")

    return token
def send_msg(token):
    s = requests.session()
    headers = {
        "Token": token,
        "Referer": "https://staging-meecnh5hre8z7dnmr6ww8ka5sd4xwt.miyachat.com/",
        "Content-Type": "application/json;charset=UTF-8"
    }
    # 个人私聊
    url = 'https://staging-meet-api.miyachat.com/im/SendMsg'
    f = Faker('zh_CN')
    data = {
        "sessionInfo": {"firstID": 724, "secondID": 725, "sessionType": 1},
        "msgContent": {"content": "@所有人"}
    }
    print(data)

    r = s.post(url=url, json=data, headers=headers)
    for i in range(1000000):
        data = {
            "sessionInfo": {"firstID": 724, "secondID": 725, "sessionType": 1},
            "msgContent": {"content": f.sentence()}
        }
        print(data)

        r = s.post(url=url, json=data, headers=headers)
        print(r.text)

        if r.text.find("msgContent") == -1:
            raise Exception("登录失败")
def init():
    with open("token.txt","r") as f:
        content = f.readline()
        print(f"read from token.txt token = {content}")

        f.close()
        return content

if __name__ == '__main__':
    token = init()
    try:
        send_msg(token)
    except:
        token = getCookie().get("value")
        with open("token.txt", "w+") as f:
            f.write(token)
            print(f"write to token.txt token = {token}")
            f.close()
        send_msg(token)

