import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Hover over Menu on demoqa.com")
@allure.description("Test to hover over Main Item 2 → SUB SUB LIST → Sub Sub Item 2")
def test_menu_hover():
    with allure.step("Launch Chrome browser"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

    try:
        with allure.step("Navigate to demoqa.com/menu"):
            driver.get("https://demoqa.com/menu")

        with allure.step("Hover over 'Main Item 2'"):
            main_item2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Main Item 2']")))
            driver.execute_script("arguments[0].scrollIntoView(true)", main_item2)
            actions.move_to_element(main_item2).perform()

        with allure.step("Hover over 'SUB SUB LIST »'"):
            sub_sub_list = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']")))
            actions.move_to_element(sub_sub_list).perform()

        with allure.step("Hover over 'Sub Sub Item 2'"):
            sub_sub_item2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sub Sub Item 2']")))
            actions.move_to_element(sub_sub_item2).perform()

        with allure.step("Print success message and attach screenshot"):
            allure.attach(driver.get_screenshot_as_png(), name="HoverSuccess", attachment_type=allure.attachment_type.PNG)
            print("Hovering completed successfully")

    finally:
        with allure.step("Close the browser"):
            driver.quit()
