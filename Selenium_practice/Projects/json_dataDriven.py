from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


json_file = 'Projects/test_data.json'

test_data = []
with open(json_file , 'r') as file:
    test_data = json.load(file)

    
for data in test_data['users']:

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)


    driver.get("https://www.saucedemo.com/")


    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"user-name")
        )
    )
    username.send_keys(data['username'])

    password = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"password")
        )
    )
    password.send_keys(data['password'])


    driver.find_element(By.ID,"login-button").click()

    time.sleep(5)

    driver.quit()




# Need chrome setup code if shown change password error



