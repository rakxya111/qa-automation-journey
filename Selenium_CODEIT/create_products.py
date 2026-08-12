from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import products
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://cloud.restroorder.com/dashboard?tab=dashboard-1")

wait = WebDriverWait(driver,20)


def click(xpath):
    wait.until(
        EC.element_to_be_clickable((By.XPATH,xpath))
    ).click()


def type_text(xpath,text):
    ele = wait.until(
        EC.visibility_of_element_located((By.XPATH,xpath))
    )
    ele.clear()
    ele.send_keys(text)


def select_category(category):

    dropdown = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,"//input[@placeholder='Select Category']/following::div[contains(@class,'indicator')][1]")
        )
    )

    dropdown.click()

    option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//div[contains(@class,'option') and normalize-space()='{category}']"
            )
        )
    )

    option.click()


def select_unit():

    unit_dropdown = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,"//input[contains(@placeholder,'Select Unit')]")
        )
    )

    unit_dropdown.click()

    default_unit = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,"//div[contains(@class,'option')]")
        )
    )

    default_unit.click()


for category, product, price in products:

    # Open Create Product page
    driver.get("https://cloud.restroorder.com/menu-item/create")

    # ---------------- General Info ----------------

    type_text("//input[@placeholder='Enter product name']", product)

    select_category(category)

    # ---------------- Units & Pricing ----------------

    click("//button[contains(.,'Units & Pricing')]")

    select_unit()

    selling_price = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH,"(//input[@value='0'])[2]")
        )
    )

    selling_price.clear()
    selling_price.send_keys(str(price))

    purchase_price = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH,"(//input[@value='0'])[3]")
        )
    )

    purchase_price.clear()
    purchase_price.send_keys(str(price))

    # ---------------- Save ----------------

    click("//button[contains(.,'Save Product')]")

    time.sleep(2)

print("All Products Created Successfully")

driver.quit()