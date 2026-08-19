from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


url = 'https://the-internet.herokuapp.com/broken_images'
browser = webdriver.Chrome()
wait = WebDriverWait(browser , 10)
browser.get(url)

browser.maximize_window()

images = wait.until(
    EC.presence_of_all_elements_located(
        (By.TAG_NAME, 'img')
    )
)

broken_images = []

for image in images:
    src = image.get_attribute("src")

    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f'Broken Image found')


if broken_images:
    print('List of Broken Images')

    for broken_image in broken_images:
        print(broken_image)
else:
    print('No Broken Images Found.')


input('Click Enter to Stop...')
browser.quit()