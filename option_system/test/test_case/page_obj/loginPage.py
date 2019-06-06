#coding: utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
	
	url = '/'

	login_username_loc = (By.NAME, "account")
	login_password_loc= (By.NAME, "password")
	login_button_loc = (By.XPATH, "//div[@class = 'form-action bg-gradient']/p")
	login_success_loc = (By.XPATH, "//*[@id='app']/div/header/div/div/div[3]/div")
	error_hint_loc = (By.XPATH, "//form/div[@class='tipMessage red']")

	clear_username_loc = (By.NAME, "account")
	clear_password_loc = (By.NAME, "password")

	def login_username(self, username):
		self.find_element(*self.login_username_loc).send_keys(username)

	def login_password(self, password):
		self.find_element(*self.login_password_loc).send_keys(password)

	def login_button(self):
		print(self.find_element(*self.login_button_loc))
		self.find_element(*self.login_button_loc).click()

	#错误提示
	def error_hint(self):
		return self.find_element(*self.error_hint_loc).text
	# 登录成功用户名	
	def login_success(self):
		return self.find_element(*self.login_success_loc).text


	def user_login(self, username = "username", password = "password"):
		
		self.open()
		self.login_username(username)
		self.login_password(password)
		self.login_button()
		sleep(1)
	
	def login_clear(self):
		self.find_element(*self.clear_username_loc).clear()
		self.find_element(*self.clear_password_loc).clear()



class forgetPassword(Page):

	url = '/signin/forget'
	
	forget_username_loc = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div/div[1]/input")
#	//*[@id="app"]/div/div/div[2]/div/div/div[1]/input
	forget_getCode_loc = (By.XPATH, "//span[text()='获取验证码']")
	forget_inputCode_loc = (By.XPATH, "//input[@placeholder='请输入验证码']") 
	forget_newPassword_loc = (By.XPATH, "//div[@class='password el-input']/input") 
	newPassword_sure_loc = (By.XPATH, "//div[@class='nextpassword el-input']/input") 
	forget_submit_loc = (By.XPATH, "//span[text()='提交']")
	forget_back_loc = (By.XPATH, "//p[text()='返回登录']")
	forget_error_loc = (By.XPATH, "//p[@class='Tips']")

	def forget_username(self, username):
		self.find_element(*self.forget_username_loc).send_keys(username)
	
	def forget_getCode(self):
		self.find_element(*self.forget_getCode_loc).click()

	def forget_inputCode(self, code):
		self.find_element(*self.forget_inputCode_loc).send_keys(code)

	def forget_newPassword(self, newpassword):
		self.find_element(*self.forget_newPassword_loc).send_keys(newpassword)

	def newPassword_sure(self, snewpassword):
		self.find_element(*self.newPassword_sure_loc).send_keys(snewpassword)

	def forget_submit(self):
		self.find_element(*self.forget_submit_loc).click()

	def forget_back(self):
		self.find_element(*self.forget_back_loc).click()
	
	def user_update_password(self, username, code, newpassword, snewpassword):
		self.open()	
		self.forget_username(username)
		self.forget_getCode()
		sleep(2)
		self.forget_inputCode(code)
		self.forget_newPassword(newpassword)
		self.newPassword_sure(snewpassword)
		self.forget_submit()





'''
# coding: utf-8

from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://dev-option.fundusd.com')
driver.find_element(By.NAME, 'account').send_keys('120')
driver.find_element(By.NAME, 'password').send_keys('123456')
driver.find_element(By.XPATH, "//div[@class='form-action bg-gradient']/p").click()
time.sleep(3)
#driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[2]/div/img[@class='picture']").text()
#driver.find_element(By.LINK_TEXT, '计划管理').click()
'''
