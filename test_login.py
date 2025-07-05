import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@allure.title("Test Login Functionality on PracticeTestAutomation")
def test_login_with_blank_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        with allure.step("Open Login Page"):
            driver.get("https://practicetestautomation.com/practice-test-login/")
            allure.attach(driver.get_screenshot_as_png(), name="Login Page", attachment_type=allure.attachment_type.PNG)

        with allure.step("Enter Username"):
            username = driver.find_element(By.ID, "username")
            username.send_keys("student")

        with allure.step("Leave Password Blank"):
            pwd = ""  
            password = driver.find_element(By.ID, "password")
            password.send_keys(pwd)

        with allure.step("Click Submit Button"):
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()
            time.sleep(2)

        with allure.step("Verify Login Result"):
            try:
                msg = driver.find_element(By.TAG_NAME, 'h1').text
                if "Logged In Successfully" in msg:
                    allure.attach(driver.get_screenshot_as_png(), name="Success Page", attachment_type=allure.attachment_type.PNG)
                    print("Login successful")
                    assert False, "Login should not be successful with blank password"
                else:
                    print("Login failed")
            except NoSuchElementException:
                allure.attach(driver.get_screenshot_as_png(), name="Failure Page", attachment_type=allure.attachment_type.PNG)
                print("Login failed: No success message found")

        if pwd.strip() == "":
            with allure.step("Check Blank Password"):
                print("Please enter a valid password")
                allure.attach("Blank password detected", name="Validation", attachment_type=allure.attachment_type.TEXT)
                assert True  

    finally:
        with allure.step("Close Browser"):
            driver.quit()
