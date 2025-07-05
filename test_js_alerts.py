import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@allure.title("Handle JavaScript Alerts on Herokuapp")
@allure.description("Test handles JS Alert, Confirm, and Prompt and verifies their behaviors.")
def test_js_alerts_handling():
    with allure.step("Launch Chrome browser"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    try:
        with allure.step("Navigate to JS Alerts demo page"):
            driver.get("https://the-internet.herokuapp.com/javascript_alerts")
            allure.attach(driver.get_screenshot_as_png(), name="Page Loaded", attachment_type=allure.attachment_type.PNG)

        with allure.step("Handle Simple JS Alert"):
            driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
            alert = driver.switch_to.alert
            alert_text = alert.text
            print("Simple Alert Text:", alert_text)
            allure.attach(alert_text, name="Simple Alert Text", attachment_type=allure.attachment_type.TEXT)
            time.sleep(2)
            alert.accept()

        with allure.step("Handle JS Confirm Alert"):
            driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
            confirm_alert = driver.switch_to.alert
            confirm_text = confirm_alert.text
            print("Confirm Alert Text:", confirm_text)
            allure.attach(confirm_text, name="Confirm Alert Text", attachment_type=allure.attachment_type.TEXT)
            time.sleep(2)
            confirm_alert.accept()

        with allure.step("Handle JS Prompt Alert"):
            driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
            prompt_alert = driver.switch_to.alert
            prompt_text = prompt_alert.text
            print("Prompt Alert Text:", prompt_text)
            allure.attach(prompt_text, name="Prompt Alert Text", attachment_type=allure.attachment_type.TEXT)
            time.sleep(2)
            prompt_alert.send_keys("Hi I'm Priya")
            time.sleep(2)
            prompt_alert.accept()

        with allure.step("All alerts handled successfully"):
            print("All alerts handled successfully")
            allure.attach("All alerts were accepted correctly.", name="Alert Result", attachment_type=allure.attachment_type.TEXT)

    finally:
        with allure.step("Close the browser"):
            driver.quit()
