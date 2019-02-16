from selenium import webdriver
import random
import time
browseone = webdriver.Chrome()


#baidu

i = 0

while i<100:
    phonnum = '1865721'+ str(random.randrange(1000,9999,2))
    browseone.get('https://passport.baidu.com/v2/?reg&tt=1545202034282&overseas=undefined&gid=B233889-DC5E-424C-8F2E-B4D42CEA7C53&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2F%3Ftn%3D62095104_15_oem_dg')
    time.sleep(1)
    browseone.find_element_by_id('#TANGRAM__PSP_3__userName').send_keys('hehan335566')
    time.sleep(1)
    browseone.find_element_by_id('#TANGRAM__PSP_3__phone').send_keys(phonnum)
    time.sleep(1)
    browseone.find_element_by_id('#TANGRAM__PSP_3__password').send_keys('tanxiaopang123')
    time.sleep(1)
    browseone.find_element_by_id('#TANGRAM__PSP_3__verifyCodeSend').click()
    time.sleep(1)
    browseone.close()
    i = i+1


#





