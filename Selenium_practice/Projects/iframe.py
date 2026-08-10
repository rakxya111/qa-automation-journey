from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://testing.qaautomationlabs.com/iframe.php"

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

browser.get(url)
browser.maximize_window()

iframe = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "iframe[title='iframe 1']")
    )
)

browser.switch_to.frame(iframe)

button = browser.find_element(
    By.CSS_SELECTOR,
    ".btn.btn-primary.btn-sm.w-100"
)

button.click()

print("Successful")

input("Click enter to exit..")
browser.quit()