from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://testing.qaautomationlabs.com/javaScript-alert.php'
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
wait = WebDriverWait(browser, 10)

promptButton = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//button[normalize-space()='Show Prompt']")
    )
)
promptButton.click()


prompt = browser.switch_to.alert
prompt_text = prompt.text
print(prompt_text)

# Send Keys
prompt.send_keys('This is Rakshya Bhuju.')
time.sleep(5)

# To cancel or dismiss
prompt.accept()


input('Click enter to exit..')
browser.quit()