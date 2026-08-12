from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time 


url = 'https://www.globalsqa.com/demo-site/datepicker/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
wait = WebDriverWait(browser , 10)

datepicker = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "datepicker2")
    )
)
datepicker.click()

current_date = datetime.now()
future_date = current_date + timedelta(days=1)


Next_day = str((future_date.day))
current_month = datetime.now().month
current_year = current_date.year

next_month = (current_month % 12) + 1
next_month_and_year = f'{next_month} / {current_year}'


# Select the Month
Month_dropdown = browser.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
select = Select(Month_dropdown)
select.select_by_value(next_month_and_year)

# Select the Year
Year_dropdown = browser.find_element(By.CSS_SELECTOR, "select[title='Change the year']")
select = Select(Year_dropdown)
select.select_by_visible_text("2025")

browser.find_element(By.LINK_TEXT, Next_day).click()

time.sleep(5)