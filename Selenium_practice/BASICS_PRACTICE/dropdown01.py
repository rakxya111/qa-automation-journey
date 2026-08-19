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
        (By.ID,"countryDropdown")
    )
)

dropdown = Select(dropdown_element)
dropdown.select_by_visible_text('India')

button = wait.until(
    EC.visibility_of_element_located(
       ( By.CSS_SELECTOR,"button[title='First Selected']")
        )
)

# Scroll the element into view : Scroll this element into the center of the screen.
browser.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    button
)

button.click()

print('Sucessfull')

input('wait')

