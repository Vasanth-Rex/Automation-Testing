import pytest
import allure
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Login Test using CSV Data on demoqa.com")
@allure.description("This test reads username and password from a CSV file and attempts login on https://demoqa.com/login")
def test_login_with_csv_data():
    with allure.step("Launch Chrome browser"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

    try:
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)

            for index, row in enumerate(reader, start=1):
                with allure.step(f"Login Attempt #{index} for username: {row['username']}"):
                    driver.get("https://demoqa.com/login")

                    user_input = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
                    driver.execute_script("arguments[0].scrollIntoView(true)", user_input)
                    ActionChains(driver).move_to_element(user_input).perform()
                    user_input.clear()
                    user_input.send_keys(row['username'])

                    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
                    ActionChains(driver).move_to_element(password_input).perform()
                    password_input.clear()
                    password_input.send_keys(row['password'])

                    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
                    ActionChains(driver).move_to_element(login_button).perform()
                    login_button.click()
                    time.sleep(2)

                    current_url = driver.current_url
                    allure.attach(driver.get_screenshot_as_png(), name=f"Login_Attempt_{index}", attachment_type=allure.attachment_type.PNG)

                    if "profile" in current_url:
                        allure.attach(f"Login successful for {row['username']}", name=f"Success_{index}", attachment_type=allure.attachment_type.TEXT)
                        driver.get("https://demoqa.com/login")
                    else:
                        allure.attach(f"Login failed for {row['username']}", name=f"Failure_{index}", attachment_type=allure.attachment_type.TEXT)
                        driver.get("https://demoqa.com/login")

    finally:
        with allure.step("Close the browser"):
            driver.quit()
