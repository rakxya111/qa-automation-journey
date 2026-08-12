from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://testing.qaautomationlabs.com/javaScript-alert.php")

wait = WebDriverWait(driver, 10)

# ---------------------------
# 1. Simple Alert
# ---------------------------
driver.find_element(By.XPATH, "//button[text()='Show Alert']").click()

# Switch to alert
alert = wait.until(EC.alert_is_present())

print("Alert Text:", alert.text)

# Click OK
alert.accept()

time.sleep(2)

# ---------------------------
# 2. Confirmation Alert
# ---------------------------
driver.find_element(By.XPATH, "//button[text()='Show Confirm']").click()

alert = wait.until(EC.alert_is_present())

print("Confirm Text:", alert.text)

# Click OK
alert.accept()

time.sleep(2)

# ---------------------------
# 3. Prompt Alert
# ---------------------------
driver.find_element(By.XPATH, "//button[text()='Show Prompt']").click()

alert = wait.until(EC.alert_is_present())

print("Prompt Text:", alert.text)

# Type your name
alert.send_keys("Roxks")

# Click OK
alert.accept()

time.sleep(3)

driver.quit()