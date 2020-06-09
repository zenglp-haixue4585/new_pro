from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# driver.get(r"https://www.baidu.com")
driver.get(r"https://account-devops.aliyun.com/rdc_login")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located, (By.XPATH, "//div[text()='阿里云 RAM 账号']"))

driver.find_element_by_xpath("//div[text()='阿里云 RAM 账号']").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located, (By.XPATH, "//input[@id='user_principal_name']"))

driver.find_element_by_xpath("//input[@id='user_principal_name']").send_keys("zenglipeng@linxuan.onaliyun.com")

driver.find_element_by_xpath("//span[@class='fm-button next-btn']").click()
time.sleep(0.5)
driver.find_element_by_xpath("//input[@id='password_ims']").send_keys("1qaz@WSX")

driver.find_element_by_xpath("//input[@type='submit']").click()

time.sleep(2)
driver.get(r"https://devops.aliyun.com/project/5ea24632862d440022a9da08/testplan/5ec24b86630aeb0021243616/group/all")
