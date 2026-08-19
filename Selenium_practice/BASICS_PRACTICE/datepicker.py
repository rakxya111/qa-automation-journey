from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time 


url = 'https://www.globalsqa.com/demo-site/datepicker/'
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
wait = WebDriverWait(browser , 10)


close_button = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']")
    )
).click()

frameLo = browser.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame']")

browser.switch_to.frame(frameLo)
time.sleep(5)
datepicker = browser.find_element(By.CSS_SELECTOR, "#datepicker").click()

current_date = datetime.now()

# If have to select the future date this would be current date + 1
next_date = current_date + timedelta(days=1)

# If have to select the past date
# previous_date = current_date + timedelta(days=-1)

formattedDate = next_date.strftime("%m / %d / %y")

browser.find_element(By.CSS_SELECTOR, "#datepicker").send_keys(formattedDate + webdriver.Keys.TAB)
time.sleep(5)

input('Click enter to exit..')
browser.quit()