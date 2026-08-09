from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://testing.qaautomationlabs.com/dropdown.php'
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wait = WebDriverWait(browser , 10)

dropdown_element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "fruitDropdown")
    )
)

select = Select(dropdown_element)
target_value = 'Mango'

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f'Selected option is {target_value}')
        break
    else:
        print(f'{target_value} not found')

# select.select_by_index(1)
# select.select_by_value('Apple')

input('Click enter to stop')