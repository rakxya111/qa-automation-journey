from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'https://demo.automationtesting.in/Resizable.html'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
wait = WebDriverWait(browser, 10)

resizeable_element = browser.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")

initial_size = browser.find_element(By.XPATH, "//div[@id='resizable']")
initial_sized_element = initial_size.size
print("Resized Element :", initial_sized_element)

action = webdriver.ActionChains(browser)
action.click_and_hold(resizeable_element).move_by_offset(100,100).release().perform()
time.sleep(5)

resized_element = initial_size.size
print("Resized Element :", resized_element)

browser.quit()