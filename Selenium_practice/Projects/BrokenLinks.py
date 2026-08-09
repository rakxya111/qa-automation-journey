from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

url = "https://jqueryui.com/"

browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

wait = WebDriverWait(browser, 10)

get_links = wait.until(
    EC.presence_of_all_elements_located(
        (By.TAG_NAME, "a")
    )
)

print(f"The total links on the page are {len(get_links)}")


for link in get_links:
    href = link.get_attribute('href')
    response = requests.get(href)

    if response.status_code >= 400:
        print(f'Broken link {href} (Status code : {response.status_code})')

input("Press Enter to close...")
browser.quit()