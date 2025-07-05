import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@allure.title("DuckDuckGo Search Test")
@allure.description("Searches for 'Amazon' on DuckDuckGo and verifies results appear.")
def test_duckduckgo_search():
    with allure.step("Launch Chrome browser"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    try:
        with allure.step("Navigate to DuckDuckGo homepage"):
            driver.get("https://duckduckgo.com")
            time.sleep(2)
            allure.attach(driver.get_screenshot_as_png(), name="Homepage", attachment_type=allure.attachment_type.PNG)

        with allure.step("Enter 'Amazon' in the search box and press Enter"):
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys("Amazon")
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            allure.attach(driver.get_screenshot_as_png(), name="Search Results", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify search results page contains 'Amazon'"):
            page_source = driver.page_source
            assert "Amazon" in page_source or "amazon" in page_source.lower(), "Amazon not found in search results"
            allure.attach("Amazon found in results", name="Search Verification", attachment_type=allure.attachment_type.TEXT)

    finally:
        with allure.step("Close the browser"):
            driver.quit()
