from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 20)


wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))


wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Recruitment']"))
).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[.//i[contains(@class,'plus')]]"))
).click()

wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))


driver.find_element(By.NAME, "firstName").send_keys("Aromal")
driver.find_element(By.NAME, "middleName").send_keys("Prakash")
driver.find_element(By.NAME, "lastName").send_keys("Bindhu")


driver.find_element(By.XPATH, "//label[text()='Email']/following::input[1]").send_keys("aromal@yopmail.com")

wait = WebDriverWait(driver, 20)

vacancy_dropdown = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[text()='Vacancy']/following::div[1]")
    )
)

vacancy_dropdown.click()
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Senior QA Lead']")
    )
).click()

driver.find_element(By.XPATH, "//label[text()='Contact Number']/following::input[1]").send_keys("9876543210")


driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
    r"C:\Users\Tester\Downloads\AromalPbResume.pdf"
)
driver.find_element(
    By.XPATH, "//label[text()='Keywords']/following::input[1]"
).send_keys("Selenium, Python, Automation")

driver.find_element(
    By.XPATH, "//textarea[@placeholder='Type here']"
).send_keys("Candidate has strong Selenium and Python skills.")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(30)

print("Candidate added successfully")
