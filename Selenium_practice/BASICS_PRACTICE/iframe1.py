from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://the-internet.herokuapp.com/iframe"

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

browser.get(url)
browser.maximize_window()

iframe = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "mce_0_ifr")
    )
)

browser.switch_to.frame(iframe)


text_editor = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "tinymce")
    )
)

text_editor.clear()
text_editor.send_keys("Hello this is rakshya bhuju.")

print("Successful")

input("Click enter to exit..")
browser.quit()