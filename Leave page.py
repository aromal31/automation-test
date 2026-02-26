from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:

    def __init__(self, driver):
        self.driver = driver

    def apply_leave(self):
        wait = WebDriverWait(self.driver, 10)


        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Leave']"))).click()

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Apply']"))).click()


        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='oxd-select-text']"))).click()

        self.driver.find_element(
            By.XPATH, "//span[text()='Casual Leave']").click()


        date_field = self.driver.find_element(
            By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
        date_field.clear()
        date_field.send_keys("2026-03-01")


        self.driver.find_element(
            By.XPATH, "//button[@type='submit']").click()


        success = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "oxd-toast")))
        assert success.is_displayed()