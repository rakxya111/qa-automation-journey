from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'https://testing.qaautomationlabs.com/slider.php'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
wait = WebDriverWait(browser, 10)


slider = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "slider1")
    )
)

action = webdriver.ActionChains(browser)
action.click_and_hold(slider).move_by_offset(60,0).release().perform()

time.sleep(5)
browser.quit()