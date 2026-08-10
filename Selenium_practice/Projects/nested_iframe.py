from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://the-internet.herokuapp.com/nested_frames"
browser = webdriver.Chrome()
wait = WebDriverWait(browser , 10)

browser.get(url)
browser.maximize_window()

# Switch to the Top Frame
browser.switch_to.frame('frame-top')

# Switch to the Middle Frame
browser.switch_to.frame('frame-middle')
content_middle = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "content")
    )
)
print('Content in the middle is : ', content_middle.text)

# Go back to the main page
browser.switch_to.default_content()

# Switch to the Bottom Frame
browser.switch_to.frame('frame-bottom')

content_bottom = wait.until(
    EC.visibility_of_element_located(
        (By.TAG_NAME,"body")
    )
)
print('Content in the bottom is : ', content_bottom.text)