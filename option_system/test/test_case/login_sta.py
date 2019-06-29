# coding: utf-8

import time
import unittest, random, sys
sys.path.append("./ models")
sys.path.append("./ page_obj")
from models.myunit import * 
from models.function import * 
from page_obj.loginPage import login, forgetPassword

class loginTest(MyTest):
		
	def user_login_verify(self, username="", password=""):
		login(self.driver).user_login(username, password)

	def test_login(self):
		#用户名、密码为空
		self.user_login_verify()
		po = login(self.driver)
		insert_img(self.driver, "login_allempty.png")
		self.assertEqual(po.error_hint(), "请输入登录邮箱/手机")
		po.login_clear()
		time.sleep(2)
			
#	def test_login1(self):
		#用户名为空,密码正确
		self.user_login_verify(password = "abcd1234")
		po = login(self.driver)
		insert_img(self.driver, "user_empty.png")
		self.assertEqual(po.error_hint(), "请输入登录邮箱/手机")
		po.login_clear()
		time.sleep(2)
	
#	def test_login2(self):
		#用户名不存在，密码为空
		character = random.choice('abcdefjhigklmnopqrstuvwxyz')
		username = "zhangsan" + character
		self.user_login_verify(username = username)
		po = login(self.driver)
		insert_img(self.driver, "wrong_username.png")
		self.assertEqual(po.error_hint(), "此账户不存在")
		po.login_clear()
		time.sleep(2)

#def test_login3(self):
		#用户名正确，密码为空
		self.user_login_verify(username = "dev@test.com")
		po = login(self.driver)
		insert_img(self.driver, "password_empty.png")
		self.assertEqual(po.error_hint(), "请输入登录密码")
		po.login_clear()
		time.sleep(2)
	
#	def test_login4(self):
		#用户名正确，密码错误
		self.user_login_verify(username = "dev@test.com", password = "000000")
		po = login(self.driver)
		insert_img(self.driver, "wrong_password.png")
		self.assertEqual(po.error_hint(), "登录密码不正确")
		po.login_clear()
		time.sleep(2)
	
#	def test_login5(self):
		#用户名不正确，密码正确
		character = random.choice('abcdefjhigklmnopqrstuvwxyz')
		username = "zhangsan" + character
		self.user_login_verify(username = username, password = "abcd1234")
		po = login(self.driver)
		insert_img(self.driver, "wrong_username.png")
		self.assertEqual(po.error_hint(), "此账户不存在")
		po.login_clear()
		time.sleep(2)
	
#	def test_login(self):
		#用户名正确，密码正确
		self.user_login_verify(username = "dev@test.com", password = "abcd1234")
		po = login(self.driver)
		insert_img(self.driver, "success_login.png")
		self.assertEqual(po.login_success(), "您好，Kate")
	
if __name__ == '__main__':

	unittest.main()
