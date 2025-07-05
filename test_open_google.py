import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@allure.title("Open Google Homepage")
def test_open_google():
    with allure.step("Set up Chrome browser with chromedriver"):
        service = Service(r"C:\Users\HP\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

    try:
        with allure.step("Navigate to Google"):
            driver.get("https://www.google.com")
            allure.attach(driver.get_screenshot_as_png(), name="Google Page", attachment_type=allure.attachment_type.PNG)
            print("Browser opened successfully")

    finally:
        with allure.step("Close the browser"):
            driver.quit()
