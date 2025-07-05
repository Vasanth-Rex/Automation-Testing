import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.title("Test Switching Between Browser Tabs on demoqa.com")
@allure.description("This test opens a new browser tab, verifies the content, then returns to the main tab.")
def test_switch_browser_windows():
    with allure.step("Launch Chrome browser"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    try:
        with allure.step("Navigate to demoqa.com/browser-windows"):
            driver.get("https://demoqa.com/browser-windows")
            main_window = driver.current_window_handle
            allure.attach(driver.get_screenshot_as_png(), name="Main Window", attachment_type=allure.attachment_type.PNG)

        with allure.step("Click 'New Tab' button to open new window"):
            driver.find_element(By.ID, "tabButton").click()
            time.sleep(2)  
            all_windows = driver.window_handles

        with allure.step("Switch to new tab and verify heading text"):
            for handle in all_windows:
                if handle != main_window:
                    driver.switch_to.window(handle)
                    break
            heading = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "sampleHeading"))
            )
            heading_text = heading.text
            print("New tab heading:", heading_text)
            allure.attach(driver.get_screenshot_as_png(), name="New Tab", attachment_type=allure.attachment_type.PNG)
            allure.attach(heading_text, name="New Tab Heading", attachment_type=allure.attachment_type.TEXT)

            assert heading_text == "This is a sample page", "Unexpected heading in new tab"

            driver.close()

        with allure.step("Switch back to main window and verify title"):
            driver.switch_to.window(main_window)
            main_tab_title = driver.title
            print("Back to main window:", main_tab_title)
            allure.attach(main_tab_title, name="Main Tab Title", attachment_type=allure.attachment_type.TEXT)
            allure.attach(driver.get_screenshot_as_png(), name="Returned to Main", attachment_type=allure.attachment_type.PNG)

    finally:
        with allure.step("Close the browser"):
            driver.quit()
