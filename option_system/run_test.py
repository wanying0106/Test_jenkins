# coding: utf-8

from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os

if __name__ == '__main__':

	now =time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './test/report/' + now + 'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream = fp,
							title = 'test report')
	discover = unittest.defaultTestLoader.discover('./test/test_case', pattern = '*_sta.py')
	runner.run(discover)
	fp.close()
