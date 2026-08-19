from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


username = 'admin'
password = 'admin'

Orginal_url = 'https://the-internet.herokuapp.com/basic_auth'

# Syntax - https://username:password@domain/path

auth_url = 'https://admin:admin@the-internet.herokuapp.com/basic_auth'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(auth_url)
wait = WebDriverWait(browser, 10)

time.sleep(5)
browser.quit()