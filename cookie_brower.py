# coding=utf-8
from selenium import webdriver
import time
from config import *
#创建浏览器
driver = webdriver.Chrome()
driver.set_window_size(1400, 900)
#读取cookie值和url
ichunqiu_cookie=COOKIE
url=URL
#处理cookie为selenium的样式
def cookies_parse(cookies):
    parsed_cookies = []
    cookies = cookies.split(';')
    for cookie in cookies:
        cookie = cookie.strip()
        name = cookie.split('=')[0]
        value = cookie.split('=')[1]
        parsed_cookies.append({'name': name, 'value': value})
    return parsed_cookies
#利用cookie登录网页
def cookie_cheat(url, cookies):
    driver.get(url)
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.get(url)
    time.sleep(10)

kk=cookies_parse(ichunqiu_cookie)
print kk
cookie_cheat(url,kk)
