from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://testing.qaautomationlabs.com/dropdown.php'
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

wait = WebDriverWait(browser , 10)

dropdown_element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "fruitDropdown")
    )
)

select = Select(dropdown_element)

# select.select_by_index(1)
select.select_by_value('Apple')

input('Click eneter to stop')