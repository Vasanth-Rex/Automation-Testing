import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@allure.title("Test Drag and Drop on jQuery UI")
def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open jQuery UI droppable demo page"):
            driver.get("https://jqueryui.com/droppable/")
            allure.attach(driver.get_screenshot_as_png(), name="Main Page", attachment_type=allure.attachment_type.PNG)

        with allure.step("Switch to iframe"):
            iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
            driver.switch_to.frame(iframe)

        with allure.step("Perform drag and drop"):
            source = driver.find_element(By.ID, "draggable")
            target = driver.find_element(By.ID, "droppable")

            actions = ActionChains(driver)
            actions.drag_and_drop(source, target).perform()
            time.sleep(2)

        with allure.step("Verify drag and drop result"):
            dropped_text = target.text
            allure.attach(driver.get_screenshot_as_png(), name="After Drop", attachment_type=allure.attachment_type.PNG)

            if dropped_text == "Dropped!":
                print(" Drag and drop successful")
                allure.attach("Drag and drop was successful", name="Result", attachment_type=allure.attachment_type.TEXT)
            else:
                print("Drag and drop failed")
                allure.attach(f"Expected 'Dropped!' but got '{dropped_text}'", name="Result", attachment_type=allure.attachment_type.TEXT)
                assert False, "Drag and drop failed"

    finally:
        with allure.step("Quit the browser"):
            driver.switch_to.default_content()
            driver.quit()
