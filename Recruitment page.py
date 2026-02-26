from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RecruitmentPage:

    def __init__(self, driver):
        self.driver = driver

    def add_candidate(self):
        wait = WebDriverWait(self.driver, 10)


        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Recruitment']"))).click()

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()=' Add ']"))).click()


        wait.until(EC.visibility_of_element_located(
            (By.NAME, "firstName"))).send_keys("John")

        self.driver.find_element(
            By.NAME, "lastName").send_keys("Doe")

        self.driver.find_element(
            By.XPATH, "//button[@type='submit']").click()


        success = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "oxd-toast")))
        assert success.is_displayed()

    def search_candidate(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Recruitment']"))).click()

        search_box = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Type for hints...']")))

        search_box.send_keys("John")

        self.driver.find_element(
            By.XPATH, "//button[@type='submit']").click()

        results = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "oxd-table-body")))

        assert results.is_displayed()