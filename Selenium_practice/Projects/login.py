import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

url = 'https://nso-app.danfesolution.com/login'
username = 'admin'
password = 'Admin@123'


driver.get(url)

username_field = wait.until(
    EC.visibility_of_element_located((By.ID, "usernameOrEmail"))
)
username_field.send_keys(username)


password_field = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password_field.send_keys(password)


login_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Sign In']")
    )
)
login_button.click()


dashboard = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h4[normalize-space()='Dashboard']")
    )
)

assert dashboard.text == "Dashboard" , 'Unsucessful'
print('Sucessfull Automation.')

driver.refresh()


print("End of script reached.")

input('Press enter to exit')






""" 
Syntax : assert <condition>

Think of assert as a checkpoint.

It asks:

"Is this condition true?"

✅ If yes, the test continues.
❌ If no, the test immediately fails with an AssertionError.

Its syntax is:

assert condition

or

assert condition, "Custom error message"

"""
