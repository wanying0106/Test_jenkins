# coding: utf-8

import time
import unittest, random, sys
sys.path.append("./ models")
sys.path.append("./ page_obj")
from models.myunit import *
from models.function import *
from page_obj.loginPage import login, forgetPassword

class forgetPasswordTest(MyTest):

	def password_forget_verify(self, username="", code="", newpassword="", snewpassword=""):
		forgetPassword(self.driver).user_update_password(username, code, newpassword, snewpassword)
		
	def test_update_password(self):
		forgetPassword(self.driver).user_update_password(username="yeah006@163.com", code="123456", newpassword="123456", snewpassword="123456")

if __name__ == '__main__':
	unittest.main()
