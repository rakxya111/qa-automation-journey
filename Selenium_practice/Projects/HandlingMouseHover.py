from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time 


url = 'https://demo.automationtesting.in/Datepicker.html'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
wait = WebDriverWait(browser , 10)



actions = webdriver.ActionChains(browser)
hover_element = browser.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
time.sleep(5)
actions.move_to_element(hover_element).perform()

browser.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()
time.sleep(5)

browser.quit()