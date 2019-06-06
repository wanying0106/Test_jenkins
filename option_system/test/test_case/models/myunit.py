# coding: utf-8

from selenium import webdriver
from .driver import browser
import unittest
import os

class MyTest(unittest.TestCase):
	
	#	insert_img(self.driver, "wrong_username.png")
	def setUp(self):
		self.driver = browser()
		self.driver.implicitly_wait(10)
		self.driver.fullscreen_window()

	def tearDown(self):
		self.driver.quit()
