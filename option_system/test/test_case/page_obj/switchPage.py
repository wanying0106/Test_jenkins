# coding: utf-8 from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class switch(Page):
	
	url = '/'

	titleBar_homePage_loc= (By.LINK_TEXT, "首页")
	titleBar_planManage_loc = (By.LINK_TEXT, "计划管理")
	titleBar_staffManage_loc = (By.LINK_TEXT, "员工管理")
	titleBar_securities_loc = (By.LINK_TEXT, "证券账户")
	titleBar_fileManage_loc = (By.LINK_TEXT, "文档管理")
	titleBar_companySetup_loc = (By.LINK_TEXT, "公司设置")
#	plan_name_loc = (By.XPATH, "//*[@id='app']/div/div/div/div/div[1]/div[1]/div/div/div/div[@class_name='el-tabs__item is-top is-active']")

	def switchTo_homePage(self):
		self.find_element(*self.titleBar_homePage_loc).click()

	def switchTo_planManage(self):
		self.find_element(*self.titleBar_planManage_loc).click()

	def switchTo_staffManage(self):
		self.find_element(*self.titleBar_staffManage_loc).click()
	
	def switchTo_securities(self):
		self.find_element(*self.titleBar_securities_loc ).click()
	
	def switchTo_fileManage(self):
		self.find_element(*self.titleBar_fileManage_loc).click()

	def switchTo_companySetup(self):
		self.find_element(*self.titleBar_companySetup_loc).click()
	'''
	def get_planName(self):
		d = self.find_element(*self.plan_name_loc).getText()
		print(d)
		return d

	def switchTo_choosePlan(self, planName):
		self.find_element(*self.titleBar_choosePlan_loc).click()
	'''
