import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Open Chrome browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://testing.qaautomationlabs.com/form.php")
time.sleep(5)
# Maximize window (optional)
driver.maximize_window()

# Explicit Wait
wait = WebDriverWait(driver, 10)


# Find the search box and type "fish"
first_name = driver.find_element(By.XPATH, "//input[@id='firstname']")
first_name.send_keys("Rakshya")
time.sleep(3)

middle_name = driver.find_element(By.XPATH, "//input[@id='middlename']")
middle_name.send_keys("noo")
time.sleep(3)

last_name = driver.find_element(By.XPATH, "//input[@id='lastname']")
last_name.send_keys("Bhuju")
time.sleep(3)

email = driver.find_element(By.XPATH, "//input[@id='email']")
email.send_keys("rakshyabhuju@gmail.com")
time.sleep(3)

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("rakshya123")
time.sleep(3)

address = driver.find_element(By.XPATH, "//textarea[@id='address']")
address.send_keys("rakshya123")
time.sleep(3)

city = driver.find_element(By.XPATH, "//input[@id='city']")
city.send_keys("Bhaktapur")
time.sleep(3)

states = driver.find_element(By.XPATH, "//input[@id='states']")
states.send_keys("Bhaktapur")
time.sleep(3)

pincode = driver.find_element(By.XPATH, "//input[@id='pincode']")
pincode.send_keys("01933893")
time.sleep(3)

submit = driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
# Press Enter



try:
    # Wait until the success message appears
    success_message = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    ).text

 

    if "Form submitted successfully" in success_message:
        print("✅ Test Passed")
    else:
        print("❌ Test Failed")

except Exception as e:
    print("❌ Success message not found.")
    print("Error:", e)



# Wait a few seconds to see results
time.sleep(5)

# Close browser
driver.quit()