from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()
wait = WebDriverWait(browser , 10)

browser.get('https://www.selenium.dev/')

browser.switch_to.new_window()

browser.get('https://playwright.dev/')


number_of_tabs = len(browser.window_handles)
print(number_of_tabs)

tabs_value = browser.window_handles
print(tabs_value)


# Provides the value of the tab
current_tab = browser.current_window_handle
print(current_tab)

element = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.getStarted_Sjon')
    )
).click()

# Provides the value of the first tab
firsttab = browser.window_handles[0]

if current_tab != firsttab:
    browser.switch_to.window(firsttab)

element1 = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH,"//span[normalize-space()='Downloads']")
    )
).click()

print('Sucessfull')
input('Click enter to exit..')



