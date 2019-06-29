# coding: utf-8

from selenium import webdriver
from time import sleep

url = 'http://dev-option.fundusd.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_name("account").send_keys("dev@test.com")
driver.find_element_by_name("password").send_keys("abcd1234")
driver.find_element_by_xpath("//div[@class = 'form-action bg-gradient']/p").click()
sleep(3)
driver.find_element_by_link_text("计划管理").click()
sleep(5)
#driver.find_element_by_link_text("员工管理").click()
#driver.find_element_by_xpath("//span[contains(text(), '授予期权')]").click()

#planname = driver.find_element_by_xpath("//div[@class='el-tabs__active-bar is-top']/div[tabindex='0']").text
planname = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div/div[1]/div[1]/div/div/div/div[2]").text
print(planname)
'''
if planname == '5':
	driver.quit()
else:
	driver.find_element_by_link_text("员工管理").click()
'''
