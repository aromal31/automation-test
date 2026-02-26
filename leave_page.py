from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 30)

wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Apply']"))).click()

leave_dropdown = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//label[text()='Leave Type']/following::div[contains(@class,'oxd-select-text')][1]")
    )
)

driver.execute_script("arguments[0].click();", leave_dropdown)

option = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='option']"))
)

driver.execute_script("arguments[0].click();", option)

from_date = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]"))
)

from_date.send_keys(Keys.CONTROL + "a")
from_date.send_keys(Keys.DELETE)
from_date.send_keys("2024-02-01")

to_date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")

to_date.send_keys(Keys.CONTROL + "a")
to_date.send_keys(Keys.DELETE)
to_date.send_keys("2024-02-03")
driver.find_element(By.XPATH, "//textarea").send_keys("Family function leave")

apply_btn = wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
)

driver.execute_script("arguments[0].click();", apply_btn)

print(" Leave applied successfully")


