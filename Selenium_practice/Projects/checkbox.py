from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'https://testing.qaautomationlabs.com/checkbox.php'
browser = webdriver.Chrome()
browser.get(url)
wait = WebDriverWait(browser, 10)
browser.maximize_window()

# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

checkboxes = wait.until(
    EC.presence_of_all_elements_located
    (
        (By.XPATH,"//input[@type='checkbox']")
    )
    )

for checkbox in checkboxes:
    browser.execute_script("arguments[0].scrollIntoView();", checkbox)
    checkbox.click()

checkbox_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox_count += 1

expected_checkbox_count = 7

assert checkbox_count == expected_checkbox_count , "Not same"
print('Same number is checked as given , Sucessfull message.')

input('Click Enter to Exit.')

