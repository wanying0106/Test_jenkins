# coding: utf-8

from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class file(Page):
	
	url = '/doc'

	file_newFile_loc = (By.XPATH, "//span[text()='新建文档库']")
