# coding: utf-8

from time import sleep
import unittest, sys
sys.path.append("./ models")
sys.path.append("./ page_obj")
from models.myunit import *
from models.function import *
from page_obj.loginPage import login
from page_obj.planPage import plan 
from page_obj.switchPage import switch
from page_obj.employeesPage import employees 

class grantProcessTest(MyTest):
	
	def test_grantProcess(self, username = "dev@test.com", password = "abcd1234"):
		# 登录系统

		login(self.driver).user_login(username, password)
		po = login(self.driver)
#		insert_img(self.driver, "success_login1.png")
		sleep(2)
		self.assertEqual(po.login_success(), "您好，Kate")
		'''	
		#切换至员工管理页面	
		switch(self.driver).switchTo_staffManage()

		#添加员工
		employees(self.driver).addEmployees(name = "测试1", state = "on", email = "123@tesr.com")
		po = employees(self.driver)	
		sleep(2)
#		self.assertEqual(po.addEmployees_success_hint(), "测试1")
		'''	
		#切换至计划管理页面
		switch(self.driver).switchTo_planManage()
		sleep(2)

		#授予新建员工期权/RSU
<<<<<<< HEAD
		plan(self.driver).user_grant(member = "测试1", matureType = "time", number = "1000")		
=======
		plan(self.driver).user_grant(member = "测试", matureType = "time", number = "1000")		
>>>>>>> 0629 pass
		sleep(2)



if __name__ == '__main__':
	unittest.main()

