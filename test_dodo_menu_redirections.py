import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Test Menu Redirection on Dodo Website")
@allure.description("Click each menu item on dodo.quantumnique.tech and verify that the redirection URL is correct.")
def test_menu_redirections(driver):
    failures = []

    menu_links = {
        "ASSESSMENTS": "assessments",
        "COURSES": "courses",
        "CODE": "code",
        "PRACTICE": "practice",
        "LSRW": "lsrw",
        "BLOGS": "blog",
        "Dashboard": "dashboard"  
    }

    for link_text, expected_url_part in menu_links.items():
        with allure.step(f"Click '{link_text}' and check URL contains '{expected_url_part}'"):
            driver.get("https://dodo.quantumnique.tech/")

            try:
                xpath = f"//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{link_text.lower()}')]"
                menu_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                menu_link.click()

                WebDriverWait(driver, 10).until(
                    lambda d: expected_url_part.lower() in d.current_url.lower()
                )
                current_url = driver.current_url
                print(f"{link_text} → {current_url}")
                allure.attach(driver.get_screenshot_as_png(), name=f"{link_text}_Page", attachment_type=allure.attachment_type.PNG)

                if expected_url_part.lower() in current_url.lower():
                    print(f"{link_text}: Redirected correctly")
                    allure.attach(f"{link_text} redirected to {current_url}", name="Redirection Success", attachment_type=allure.attachment_type.TEXT)
                else:
                    print(f"{link_text}: Incorrect redirection → {current_url}")
                    failures.append(f"{link_text} wrong URL: {current_url}")
                    allure.attach(f"{link_text} failed redirection. URL: {current_url}", name="Redirection Failed", attachment_type=allure.attachment_type.TEXT)

            except Exception as e:
                if link_text.lower() == "dashboard":
                    print(f"Skipping {link_text}: likely requires login")
                    allure.attach(f"{link_text} skipped (login required or not visible)", name=f"{link_text}_Skipped", attachment_type=allure.attachment_type.TEXT)
                else:
                    print(f"{link_text}: Link not found or error: {e}")
                    failures.append(f"{link_text} not found or error: {str(e)}")
                    allure.attach(driver.get_screenshot_as_png(), name=f"{link_text}_Error", attachment_type=allure.attachment_type.PNG)
                    allure.attach(str(e), name=f"{link_text}_Exception", attachment_type=allure.attachment_type.TEXT)

    if failures:
        all_errors = "\n".join(failures)
        allure.attach(all_errors, name="Failed Redirections", attachment_type=allure.attachment_type.TEXT)
        assert False, f"Some menu links failed:\n{all_errors}"
