from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time


# Handling the CSV File
csv_file = 'Practice/Book.csv'
test_data = []

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file) 

    for row in reader:
        test_data.append(row)


for data in test_data:

    url = 'https://nso-app.danfesolution.com/login'
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get(url)


    username_field = wait.until(
        EC.visibility_of_element_located((By.ID, "usernameOrEmail"))
    )
    username_field.send_keys(data['username'])


    password_field = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_field.send_keys(data["password"])


    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Sign In']")
        )
    )
    login_button.click()


    if data['expected'] == 'sucess':

        dashboard = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h4[normalize-space()='Dashboard']")
        ))

        assert dashboard.text == "Dashboard" 

    elif data['expected'] == 'error':
        error = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,"//div[@role='alert']")
            )
        )

        assert error.is_displayed()

    elif data['expected'] == 'validation':
        username_error = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,"//div[normalize-space()='Username or email is required']")
            )
        )

        password_error = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,"//div[normalize-space()='Password is required']")
            )
        )

        assert username_error.is_displayed()
        assert password_error.is_displayed()



input('End of script reached : Press enter to exit')

driver.quit()





