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

datepicker = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "datepicker2")
    )
)
datepicker.click()

current_date = datetime.now()
future_date = current_date + timedelta(days=1)

future_month = future_date.month
future_year = future_date.year
future_day = str(future_date.day)

month_year = f"{future_month}/{future_year}"

change_month = browser.find_element(
    By.CSS_SELECTOR,
    "select[title='Change the month']"
)
select_month = Select(change_month)
select_month.select_by_value(month_year)


change_year = browser.find_element(
    By.CSS_SELECTOR,
    "select[title='Change the year']"
)
select_year = Select(change_year)
select_year.select_by_visible_text(str(future_year))


browser.find_element(By.LINK_TEXT, future_day).click()
time.sleep(5)

browser.quit()
