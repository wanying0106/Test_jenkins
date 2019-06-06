# coding: utf-8

from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class employees(Page):
	
	url = "/"

	employees_add_loc = (By.XPATH, "//*[@id='member-view']/div[1]/div[1]/button[1]/span")
	employees_add_name_loc = (By.XPATH, "//*[@placeholder='请输入员工姓名']")
	employees_add_state_loc = (By.XPATH, "//*[@placeholder='状态']")
	employees_state_on_loc = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span")
	employees_state_out_loc = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[2]/span")
	employees_add_time_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/input")
	employees_add_timeChoose_loc = (By.XPATH, "//*[@class='available today']")
	employees_add_email_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[3]/div/div/input")
	employees_add_certificatesType_loc = (By.XPATH, "//*[@id='cert_type']/div/div[1]/div/input")
	employees_add_certificatesNumber_loc = (By.XPATH, "//*[@id='cert_type']/div/div[2]/div/input")
	employees_add_complete_loc = (By.XPATH, "//*[@id='block']/div/div/div[2]/div/form/div[2]/div[9]/button/span")
	employeesAdd_error_loc = (By.XPATH, "//*[@class='tipMessage']")
#	employeesAdd_success_loc = (By.XPATH, "//*[@id='member-view']/div[1]/div[3]/div/div[3]/table/tbody/tr[1]/td[3]/div/span")


	def to_addEmployees(self):
		self.find_element(*self.employees_add_loc).click()

	def addEmployees_name(self, name):
		self.find_element(*self.employees_add_name_loc).send_keys(name)
		
	def addEmployees_state(self, state):
		self.find_element(*self.employees_add_state_loc).click()
		if state == "on":
			self.find_element(*self.employees_state_on_loc).click()
		else:
			self.find_element(*self.employees_state_out_loc).click()

	def addEmployees_time(self):
		self.find_element(*self.employees_add_time_loc).click()
		self.find_element(*self.employees_add_timeChoose_loc).click()

	def addEmployees_email(self, email):
		self.find_element(*self.employees_add_email_loc).send_keys(email)
	
	def addEmployees_complete(self):
		self.find_element(*self.employees_add_complete_loc).click()

	def addEmployees_error_hint(self):
		self.find_element(*self.employeesAdd_error_loc).text

#	def addEmployees_success_hint(self):
#		self.find_element(*self.employeesAdd_success_loc).is_displayed()

	def addEmployees(self, name = "name", state = "state", email = "email"):
		self.to_addEmployees()
		self.addEmployees_name(name)
		self.addEmployees_state(state)
		self.addEmployees_time()
		self.addEmployees_email(email)
		self.addEmployees_complete()
		sleep(2)	
