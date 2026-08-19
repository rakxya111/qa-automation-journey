from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'https://the-internet.herokuapp.com/drag_and_drop'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
wait = WebDriverWait(browser, 10)


source = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "column-a")
    )
)

destination = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "column-b")
    )
)

actions = webdriver.ActionChains(browser)
actions.drag_and_drop(source , destination).perform()

time.sleep(5)
browser.quit()