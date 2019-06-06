from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

lists = {'http://127.0.0.1:4444/wb/hub': 'Chrome'}


for host, browser in lists.items():
	print(host, browser)
	driver = Remote(command_executor = host,
					desired_capabilities={'platform': 'ANY',
										'browserName': browser,
										'version': '',
										'javascriptEnabled': True
										}
					)

	driver.get('http://www.baidu.com')
	


'''
driver = Remote(command_executor='http://10.0.2.16:5556/wd/hub',
				desired_capabilities={'platform': 'ANY',
									'browserName': 'chrome',
									'version': '',
									'javascriptEnabled': True
									}
				)

driver.get('http://www.baidu.com')


for host, browser in lists.items():
	print(host, browser)
	driver = Remote(command_executor = host,
					desired_capabilities={'platform': 'ANY',
										'browserName': browser,
										'version': '',
										'javascriptEnabled': True
										}
					)

	driver.get('http://www.baidu.com')
'''
