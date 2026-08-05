from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://rakshyabhuju.com.np/')
browser.maximize_window()

title = browser.title
print(title)