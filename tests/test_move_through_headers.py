from selenium.webdriver.common.by import By
import pytest
import logging
from utils.webdriver_utils import hover_over_elements  # Import your utility function

@pytest.mark.move_through_headers
def test_move_through_headers(browser):
    logging.info("** Executing test_move_through_headers **")

    # Locate the elements for the main menu items
    products = browser.find_element(By.XPATH, "//div[@id='w-dropdown-toggle-0']/child::div[text()='Products']")
    solutions = browser.find_element(By.XPATH, "//div[@id='w-dropdown-toggle-5']/child::div[text()='Solutions']")
    resources = browser.find_element(By.XPATH, "//div[@id='w-dropdown-toggle-20']/child::div[text()='Resources']")
    basecamp = browser.find_element(By.XPATH, "(//a[text()='Basecamp'])[1]")
    watch_demo = browser.find_element(By.XPATH, "(//a[@href='/sign-in'])[1]/preceding-sibling::a")
    sign_in = browser.find_element(By.XPATH, "(//a[@href='/sign-in'])[1]")

    # Prepare a list of elements and their names for logging
    elements_to_hover = [
        (products, 'Products'),
        (solutions, 'Solutions'),
        (resources, 'Resources'),
        (basecamp, 'Basecamp'),
        (watch_demo, 'Watch Demo'),
        (sign_in, 'Sign In')
    ]

    # Use the utility function to hover over the elements
    hover_over_elements(browser, elements_to_hover)

    logging.info("** test_move_through_headers executed successfully **")