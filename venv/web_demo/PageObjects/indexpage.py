# coding: utf-8
# Author：zlp
# Date ：2020/5/25
# Tool ：PyCharm


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# from Common.basepage import BasePage

from PageObjects import new_page

driver = BasePage(webdriver.Chrome())



# driver.get(r"https://www.baidu.com")
driver.get(r"https://account-devops.aliyun.com/rdc_login")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located, (By.XPATH, "//div[text()='阿里云 RAM 账号']"))
