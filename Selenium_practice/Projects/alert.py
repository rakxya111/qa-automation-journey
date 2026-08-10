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

alertButton = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//button[normalize-space()='Show Alert']")
    )
)
alertButton.click()
time.sleep(5)

alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)

alert.accept()


input('Click enter to exit..')
browser.quit()