from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://testing.qaautomationlabs.com/web-table.php"

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

browser.get(url)
browser.maximize_window()

target_value = "John Doe"

# Find the row containing John Doe
row = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, f"//tr[td[normalize-space()='{target_value}']]")
    )
)

# Get all cells inside John Doe's row
cells = row.find_elements(By.TAG_NAME, "td")

# 3rd column = Action column
action_cell = cells[2]

# Find Edit button inside the Action column
edit_button = action_cell.find_element(
    By.XPATH,
    "//button[@aria-label='Edit John Doe']"
)


# Scroll Edit button to the middle of the screen
browser.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    edit_button
)

# Click Edit
edit_button.click()

print("Successful")

input("Click enter to exit..")

browser.quit()