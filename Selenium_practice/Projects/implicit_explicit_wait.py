from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys('standard_user')
driver.find_element(By.ID,"password").send_keys('secret_sauce')
driver.find_element(By.ID,"login-button").click()

driver.quit()

"""
This is implicit wait this would wait globally while explicit wait we have been using since begining.
"""




