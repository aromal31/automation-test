from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
# def login(driver):
#     wait = WebDriverWait(driver, 20)


wait = WebDriverWait(driver, 20)

username = wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# time.sleep(15)

print("Logged in successfully — Home page is displayed")