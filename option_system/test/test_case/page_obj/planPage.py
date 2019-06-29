# coding: utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class plan(Page):
	
	url = "/"
	
	#定义每一个元素的位置
	plan_newPlan_loc = (By.XPATH, "//*[@id='app']/div/div/div/div[2]/div/div/div/div[1]/div[2]/button/span")
	newPlan_name_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[1]/div/div/input")
	newPlan_type_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[2]/div/div/div/input")
	newPlan_typeChose_option_loc = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span")
	newPlan_typeChose_rsu_loc = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[2]/span")
<<<<<<< HEAD
	newPlan_ExercisePrice_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[3]/div/div/div/input")
	newPlan_ExercisePrice_need_loc = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]/span")
	newPlan_ExercisePrice_no_loc = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[2]/span")
	newPlan_planNumber_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[4]/div/div/input")
	newPlan_complete_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[6]/button/span")
	newPlan_success_loc = (By.XPATH, "//*[@id='app']/div/div/div/div/div[1]/div[1]/div/div/div/div[2]")
	plan_edit_loc = (By.XPATH, "//*[@id='app']/div/div/div/div/div[2]/div[1]/div[2]/button")
	plan_editPlan_loc = (By.XPATH, "/html/body/ul/li[1]")
	plan_deletePlan_loc = (By.XPATH, "/html/body/ul/li[2]")
	plan_deleteSure_loc = (By.XPATH, "/html/body/div[4]/div/div[3]/button[2]/span")
	error_hint_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[5]")
	typeChoose_null_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[2]/div/div/div/input")
	priceChoose_null_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[3]/div/div/div/input")
	newPlan_close_loc = (By.XPATH, "//*[@id='block']/div/div/div[1]/button/i")
=======
#	newPlan_ExercisePrice_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[3]/div/div/div/input")
#	newPlan_ExercisePrice_need_loc = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]/span")
#	newPlan_ExercisePrice_no_loc = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[2]/span")
	newPlan_planNumber_loc = (By.XPATH, "//input[@placeholder='请输入计划总股数']")
	newPlan_complete_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[5]/button/span")
	newPlan_success_loc = (By.XPATH, "//*[@id='app']/div/div/div/div/div[1]/div[1]/div/div/div/div[2]")
	plan_edit_loc = (By.XPATH, "//*[contains(text(),'编辑')]")
	plan_editPlan_loc = (By.XPATH, "//li[text()='编辑计划']")
	plan_deletePlan_loc = (By.XPATH, "//li[text()='删除计划']")
	plan_deleteSure_loc = (By.XPATH, "//*[contains(text(),'确定')]")
	error_hint_loc = (By.XPATH, "//div[@class='tipMessage']")
	typeChoose_null_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[2]/div/div/div/input")
	priceChoose_null_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[3]/div/div/div/input")
	newPlan_close_loc = (By.XPATH, "//*[@id='block']/div/div/div[1]/button/i")
	default_plan_loc = (By.XPATH, "//*[@id='app']/div/div/div/div/div[1]/div[1]/div/div/div/div[2]")
>>>>>>> 0629 pass

	#期权/RSU
	grant_button_loc = (By.XPATH, "//*[@id='app']/div/div/div/div/div[2]/div[1]/button/span")	
	grant_member_loc = (By.XPATH, "//*[@placeholder='请选择授予员工']")	
<<<<<<< HEAD
	grant_member_choose_loc = (By.XPATH, "//span[text()='测试1']")	
#	/html/body/div[5]/div[1]/div[1]/ul/li[31]
=======
	grant_member_choose_loc = (By.XPATH, "//li/span[text()='测试']")
>>>>>>> 0629 pass
	grant_time_loc = (By.XPATH, "//*[@placeholder='RSU授予日期']")	
	grant_time_choose_loc = (By.XPATH, "//*[@class='available today']")	
	grant_effect_time_loc = (By.XPATH, "//*[@placeholder='RSU计算开始日期']")	
	effect_time_choose_loc = (By.XPATH, "//*[@class='available today']")	
	grant_matureType_loc = (By.XPATH, "//*[@placeholder='请选择RSU成熟方式']")	
	matureType_time_loc = (By.XPATH, "/html/body/div[@class='el-select-dropdown el-popper']/div[1]/div[1]/ul/li[1]/div")	
	matureType_other_loc = (By.XPATH, "/html/body/div[6]/div[1]/div[1]/ul/li[2]/div")	
	grant_next_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[2]/button/span")	
	grant_number_loc = (By.XPATH, "//*[@placeholder='请填写授予数量']")	
	grant_rule_loc = (By.LINK_TEXT, "使用模板快速生成规则")	
	grant_rule_choose_loc = (By.XPATH, "//*[@class='el-popover el-popper']/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]/div")
	grant_complete_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[2]/button[2]/span")	
	grant_error_loc = (By.XPATH, "//*[@class='tipMessage']")	

<<<<<<< HEAD
=======

>>>>>>> 0629 pass
	#定义执行操作
	def plan_newPlan(self):
		self.find_element(*self.plan_newPlan_loc).click()

	def newPlan_name(self, planName):
		self.find_element(*self.newPlan_name_loc).send_keys(planName)

	def newPlan_type(self, planType):
		self.find_element(*self.newPlan_type_loc).click()
		if planType == "option":
			self.find_element(*self.newPlan_typeChose_option_loc).click()
		elif planType == "rsu":
			self.find_element(*self.newPlan_typeChose_rsu_loc).click()
		else:
			self.find_element(*self.typeChoose_null_loc).click()
	
<<<<<<< HEAD
	def newPlan_ExercisePrice(self, ExercisePriceType):
		self.find_element(*self.newPlan_ExercisePrice_loc).click()
		if ExercisePriceType == "need":
			self.find_element(*self.newPlan_ExercisePrice_need_loc).click()
		elif ExercisePriceType == "no":
			self.find_element(*self.newPlan_ExercisePrice_no_loc).click()
		else:
			self.find_element(*self.priceChoose_null_loc).click()

=======
>>>>>>> 0629 pass
	def newPlan_number(self, planNumber):
		self.find_element(*self.newPlan_planNumber_loc).send_keys(planNumber)
		
	def newPlan_complete(self):
		self.find_element(*self.newPlan_complete_loc).click()

	def newPlan_success(self):
		return self.find_element(*self.newPlan_success_loc).text
	
	def plan_edit(self, editType):
		self.find_element(*self.plan_edit_loc).click()
<<<<<<< HEAD
=======
		sleep(2)
>>>>>>> 0629 pass
		if editType == "edit":
			self.find_element(*self.plan_editPlan_loc).click()
		elif editType == "delete":
			self.find_element(*self.plan_deletePlan_loc).click()
			self.find_element(*self.plan_deleteSure_loc).click()

	def error_hint(self):
		return self.find_element(*self.error_hint_loc).text
		
	def newPlan_close(self):
		self.find_element(*self.newPlan_close_loc).click()

	def grant_click(self):
		self.find_element(*self.grant_button_loc).click()

<<<<<<< HEAD
	def grant_member(self, member):
		self.find_element(*self.grant_member_loc).send_keys(member)
		sleep(1)
=======
	def default_plan_name(self):
		name = self.find_element(*self.default_plan_loc).text
		return name

	def grant_member(self, member):
		self.find_element(*self.grant_member_loc).send_keys(member)
		sleep(3)
>>>>>>> 0629 pass
		self.find_element(*self.grant_member_choose_loc).click()

	def grant_time(self):
		self.find_element(*self.grant_time_loc).click()
<<<<<<< HEAD
=======
		sleep(1)
>>>>>>> 0629 pass
		self.find_element(*self.grant_time_choose_loc).click()

	def effect_time(self):
		self.find_element(*self.grant_effect_time_loc).click()
<<<<<<< HEAD
=======
		sleep(1)
>>>>>>> 0629 pass
		self.find_element(*self.effect_time_choose_loc).click()

	def grant_matureType(self, matureType):
		self.find_element(*self.grant_matureType_loc).click()
		if matureType == "time":
			self.find_element(*self.matureType_time_loc).click()
		else:
			self.find_element(*self.matureType_other_loc).click()
		
	def grant_next(self):
		self.find_element(*self.grant_next_loc).click()

	def grant_number(self, number):
		self.find_element(*self.grant_number_loc).send_keys(number)

	def grant_rule(self):
		self.find_element(*self.grant_rule_loc).click()
		sleep(1)
		self.find_element(*self.grant_rule_choose_loc).click()
		sleep(1)

	def grant_complete(self):
		self.find_element(*self.grant_complete_loc).click()

	def grant_error(self):
		self.find_element(*self.grant_error_loc).text
		

<<<<<<< HEAD
	def user_newPlan(self, planName = "planName", planType = "planType", ExercisePriceType = "ExercisePriceType", planNumber = "planNumber"):
=======
	def user_newPlan(self, planName = "planName", planType = "planType", planNumber = "planNumber"):
>>>>>>> 0629 pass
		self.plan_newPlan()
		self.newPlan_name(planName)
		self.newPlan_type(planType)
		sleep(3)
<<<<<<< HEAD
		self.newPlan_ExercisePrice(ExercisePriceType)
=======
>>>>>>> 0629 pass
		self.newPlan_number(planNumber)
		self.newPlan_complete()
		sleep(2)

	def user_editPlan(self, planName = "planName", planNumber = "planNumber"):
		self.find_element(*self.newPlan_name_loc).clear()
		sleep(1)
		self.newPlan_name(planName)
		sleep(1)
		self.newPlan_complete()
		sleep(1)
#		self.newPlan_type(planType)

	def user_grant(self, member, matureType, number):
		self.grant_click()
		self.grant_member(member)
		sleep(2)
		self.grant_time()
		sleep(2)
		self.effect_time()
		sleep(2)
		self.grant_matureType(matureType)
		self.grant_next()
		sleep(2)
		self.grant_number(number)
		self.grant_rule()
		sleep(2)
		self.grant_complete()
