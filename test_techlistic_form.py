import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Test Techlistic Form Input")
def test_techlistic_form():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open Techlistic Practice Form page"):
            driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
            allure.attach(driver.get_screenshot_as_png(), name="Opened Form", attachment_type=allure.attachment_type.PNG)

        wait = WebDriverWait(driver, 10)

        with allure.step("Enter First Name"):
            firstname = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[1]")))
            firstname.send_keys("Priya")
            time.sleep(1)
            allure.attach(driver.get_screenshot_as_png(), name="First Name Entered", attachment_type=allure.attachment_type.PNG)

        with allure.step("Enter Last Name"):
            lastname = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[2]")))
            lastname.send_keys("R")
            time.sleep(1)
            allure.attach(driver.get_screenshot_as_png(), name="Last Name Entered", attachment_type=allure.attachment_type.PNG)

    finally:
        with allure.step("Close the browser"):
            driver.quit()
