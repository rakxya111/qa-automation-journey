from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://testing.qaautomationlabs.com/web-table.php'
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
browser.get(url)
browser.maximize_window()

# find the table
table =  wait.until(
    EC.presence_of_all_elements_located(
        (By.ID, 'dataTable')
    )
)

# find rows in the table
rows = wait.until(
    EC.presence_of_all_elements_located(
        (By.TAG_NAME, 'tr')
    )
)

target_value = 'John Doe'
found = False

# Loop row in rows
for row in rows:
    cells = wait.until(
    EC.presence_of_all_elements_located(
        (By.TAG_NAME, 'td')
    ))

    for cell in cells:
        if target_value in cell.text:
            print(f'Found value {target_value}')
            found = True
            break

    if found:
        break
    else:
        print(f'{target_value} not found')


print("sucessful")
input('Click enter to exit..')


