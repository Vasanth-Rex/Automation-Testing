import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Test Browser Navigation with Google and Wikipedia")
@allure.description("Open Google, go to Wikipedia, navigate back, forward, and refresh. Capture titles and steps.")
def test_browser_navigation():
    with allure.step("Launch Chrome browser"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    try:
        with allure.step("Navigate to Google and capture title"):
            driver.get("https://www.google.com")
            google_title = driver.title
            print("Title1:", google_title)
            allure.attach(google_title, name="Google Title", attachment_type=allure.attachment_type.TEXT)
            allure.attach(driver.get_screenshot_as_png(), name="Google Page", attachment_type=allure.attachment_type.PNG)

        with allure.step("Navigate to Wikipedia and capture title"):
            driver.get("https://www.wikipedia.org/")
            wiki_title = driver.title
            print("Title2:", wiki_title)
            allure.attach(wiki_title, name="Wikipedia Title", attachment_type=allure.attachment_type.TEXT)
            allure.attach(driver.get_screenshot_as_png(), name="Wikipedia Page", attachment_type=allure.attachment_type.PNG)

        with allure.step("Navigate back and verify title"):
            driver.back()
            back_title = driver.title
            print("Back to:", back_title)
            allure.attach(back_title, name="Back Page Title", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Navigate forward and verify title"):
            driver.forward()
            forward_title = driver.title
            print("Forward:", forward_title)
            allure.attach(forward_title, name="Forward Page Title", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Refresh the page"):
            driver.refresh()
            print("Page refreshed")
            allure.attach(driver.get_screenshot_as_png(), name="Refreshed Page", attachment_type=allure.attachment_type.PNG)

        time.sleep(2)

    finally:
        with allure.step("Close the browser"):
            driver.quit()
