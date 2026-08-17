from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'https://nso-app.danfesolution.com/login'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
wait = WebDriverWait(browser, 10)


# Login

username = wait.until(
    EC.visibility_of_element_located(
        (By.ID,"usernameOrEmail")
    )
)

username.send_keys('admin')


password = wait.until(
    EC.visibility_of_element_located(
        (By.ID,"password")
    )
)

password.send_keys('Admin@123')


click_login = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR,"button[type='submit']")
    )
)

click_login.click()


dashboard = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,".countit-page-title")
    )
)

assert dashboard.text == "Today at Pashmina" , 'Unsucessful Automation'
print('Sucessfull Automation.')


browser.quit()

