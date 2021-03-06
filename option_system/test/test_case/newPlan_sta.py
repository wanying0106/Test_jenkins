# coding: utf-8

import time
import unittest, sys
sys.path.append("./ models")
sys.path.append("./ page_obj")
from models.myunit import *
from models.function import *
from page_obj.loginPage import login
from page_obj.planPage import plan
from page_obj.switchPage import switch

class newPlanTest(MyTest):
	
	def user_newPlan_verify(self, planName = "", planType = "", planNumber = ""):
		plan(self.driver).user_newPlan(planName, planType, planNumber)

	def test_newPlan(self, username = "dev@test.com", password = "abcd1234"):
		login(self.driver).user_login(username, password)
		po = login(self.driver)
		insert_img(self.driver, "success_login.png")
		time.sleep(3)
		self.assertEqual(po.login_success(), "您好，Kate")

		#表单全部为空
		self.user_newPlan_verify(planName = "", planType = "", planNumber = "")
		po1 = plan(self.driver)
		insert_img(self.driver, "plan_allempty.png")
		self.assertEqual(po1.error_hint(), "请填写计划名称")
		po1.newPlan_close()
		time.sleep(2)

		#仅填写计划名称
		self.user_newPlan_verify(planName = "5", planType = "", planNumber = "")
		po1 = plan(self.driver)
		insert_img(self.driver, "plan_onlyname.png")
		self.assertEqual(po1.error_hint(), "请选择计划类型")
		po1.newPlan_close()
		time.sleep(2)
	
		#不填写计划数量
		self.user_newPlan_verify(planName = "5", planType = "option", planNumber = "")
		po1 = plan(self.driver)
		insert_img(self.driver, "plan_noNumber.png")
		self.assertEqual(po1.error_hint(), "请填写计划总股数")
		po1.newPlan_close()
		time.sleep(2)

		#新建成功
		self.user_newPlan_verify(planName = "5", planType = "option",planNumber = "300")
		po1 = plan(self.driver)
		time.sleep(2)
		switch(self.driver).switchTo_planManage()
		time.sleep(2)
		insert_img(self.driver, "plan_success.png")
		time.sleep(2)
		self.assertEqual(po1.default_plan_name(), '5')
#		print(po1.default_plan_name())
		switch(self.driver).switchTo_homePage()
		time.sleep(2)

		#新建计划重名
		self.user_newPlan_verify(planName = "5", planType = "option", planNumber = "300")
		po1 = plan(self.driver)
		insert_img(self.driver, "plan_sameName.png")
		self.assertEqual(po1.error_hint(), "计划名称已存在")
		po1.newPlan_close()
		time.sleep(2)

		#编辑计划
		switch(self.driver).switchTo_planManage()
		time.sleep(2)
		po1 = plan(self.driver)
		po1.plan_edit(editType = "edit")
		time.sleep(2)
		po1.user_editPlan(planName = "6")
		time.sleep(2)
		self.assertEqual(po1.default_plan_name(), '6')
#		print(po1.default_plan_name())

		#删除计划
		po1 = plan(self.driver)
		po1.plan_edit(editType = "delete")
		time.sleep(2)
		self.assertNotEqual(po1.default_plan_name(), '6')
#		print(po1.default_plan_name())
			

if __name__ == '__main__':
	unittest.main()
