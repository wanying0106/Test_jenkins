# coding: utf-8

from selenium import webdriver

def browser():
	driver = webdriver.Chrome()
	return driver

if __name__ == '__main__':
	dr = browser()
	dr.get("http://dev-option.fundusd.com/")
	dr.fullscreen_window()
	dr.quit()
