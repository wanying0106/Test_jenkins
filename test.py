# coding: utf-8
from time import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys("sousuo")
driver.implicitly_wait(30)
