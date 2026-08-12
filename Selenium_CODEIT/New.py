from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

actual_value = driver.title
excepted = "OrangeHRM"


driver.maximize_window()
time.sleep(2)


assert actual_value == excepted , "Expected vs actual value doesnot match"
print('Ypu have reached to login page')


user_name = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
user_name.send_keys('Admin')
print("We have enetered the username")


password = driver.find_element(By.XPATH,"//input[@placeholder='Password']")
password.send_keys('admin123')
print('We have entered the password.')


time.sleep(5)

login = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
login.click()


expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
actual_url = driver.current_url
assert actual_url == expected_url , "Test Fail user is not logged In."
print("Sucessfull Login.")