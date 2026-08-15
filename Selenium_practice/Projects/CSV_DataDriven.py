from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


csv_file = 'Projects/dataa.csv'

test_data = []


with open(csv_file , 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        test_data.append(row)

print(test_data)

for data in test_data:

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)


    driver.get("https://www.saucedemo.com/")


    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"user-name")
        )
    )
    username.send_keys(data['ï»¿username'])

    password = wait.until(
        EC.visibility_of_element_located(
            (By.ID,"password")
        )
    )
    password.send_keys(data['password'])


    driver.find_element(By.ID,"login-button").click()

    driver.quit()








