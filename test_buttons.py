import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Test Mouse Button Actions on DemoQA")
def test_buttons():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    try:
        with allure.step("Open https://demoqa.com/buttons"):
            driver.get("https://demoqa.com/buttons")
            allure.attach(driver.get_screenshot_as_png(), name="Opened Page", attachment_type=allure.attachment_type.PNG)

        with allure.step("Perform double-click on the button"):
            double_click_button = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
            actions.move_to_element(double_click_button).double_click().perform()
            double_message = wait.until(EC.visibility_of_element_located((By.ID, "doubleClickMessage"))).text
            allure.attach(driver.get_screenshot_as_png(), name="Double Click", attachment_type=allure.attachment_type.PNG)
            assert "You have done a double click" in double_message

        with allure.step("Perform right-click on the button"):
            right_click_button = wait.until(EC.element_to_be_clickable((By.ID, "rightClickBtn")))
            actions.context_click(right_click_button).perform()
            right_message = wait.until(EC.visibility_of_element_located((By.ID, "rightClickMessage"))).text
            allure.attach(driver.get_screenshot_as_png(), name="Right Click", attachment_type=allure.attachment_type.PNG)
            assert "You have done a right click" in right_message

        with allure.step("Click the 'Click Me' button"):
            click_me_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click Me']")))
            click_me_button.click()
            dynamic_message = wait.until(EC.visibility_of_element_located((By.ID, "dynamicClickMessage"))).text
            allure.attach(driver.get_screenshot_as_png(), name="Click Me", attachment_type=allure.attachment_type.PNG)
            assert "You have done a dynamic click" in dynamic_message

    finally:
        with allure.step("Close the browser"):
            driver.quit()
