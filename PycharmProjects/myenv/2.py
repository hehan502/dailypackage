from selenium import webdriver
from time import *

driver = webdriver.Chrome()
driver.get('https://www.sina.com.cn')
driver.maximize_window()
sleep(2)
driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[5]/ul[1]/li[1]/a/b').click()
sleep(3)
driver.find_element_by_name('username').send_keys('18657334425')
sleep(0.5)
driver.find_element_by_name('password').send_keys('11215454aad')
