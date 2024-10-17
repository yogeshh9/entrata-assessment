from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from utils.webdriver_utils import wait_for_element
import logging
import pytest

@pytest.mark.move_to_products
def test_move_to_products(browser):
    # Log the start of the test function execution
    logging.info("** Executing test_move_to_products **")

    actions = ActionChains(browser)

    # Locate and hover over 'Products'
    products = wait_for_element(browser, By.XPATH, "//div[text()='Products']", EC.visibility_of_element_located)
    actions.move_to_element(products).perform()
    logging.info("Hovered over 'Products'.")

    # Locate and hover over 'Accounting'
    accounting = wait_for_element(browser, By.LINK_TEXT, "Accounting", EC.visibility_of_element_located)
    actions.move_to_element(accounting).perform()
    logging.info("Hovered over 'Accounting'.")

    # Wait for 'Bill Pay' to be clickable
    bill_pay = wait_for_element(browser, By.LINK_TEXT, "Bill Pay", condition=EC.element_to_be_clickable)

    # Click on 'Bill Pay'
    actions.move_to_element(bill_pay).click().perform()
    logging.info("Clicked on 'Bill Pay'.")

    # Wait for the URL to change
    browser.implicitly_wait(10)

    # Log the current URL
    current_url = browser.current_url
    expected_url = "https://www.entrata.com/products/billpay"
    logging.info("Current URL after clicking: %s", current_url)

    # Assert the current URL matches the expected URL
    try:
        assert current_url == expected_url
        logging.info("URL verification successful. Expected and actual URLs match.")
    except AssertionError:
        logging.error(f"Expected URL '{expected_url}' but got '{current_url}'.")

    finally:
        logging.info("** test_open_bill executed successfully **")


