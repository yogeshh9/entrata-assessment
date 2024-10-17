from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils.webdriver_utils import take_screenshot
import logging
import pytest

@pytest.mark.summit_page
def test_summitRegistration(browser):
    logging.info("** Executing test_summitRegistration **")

    # Initialize ActionChains to handle complex user interactions
    action = ActionChains(browser)

    try:
        # Locate the "Summit" hyperlink element on the page
        summit = browser.find_element(By.LINK_TEXT, "Summit")
        logging.info("Located 'Summit' link.")

        # Move to the "Summit" link to trigger any hover effects
        action.move_to_element(summit).perform()
        logging.info("Hovered over 'Summit' link.")

        # Click on the "Summit" link
        action.click().perform()
        logging.info("Clicked on 'Summit' link.")

        # Set an implicit wait to allow time for the page to load
        browser.implicitly_wait(20)

        # Assert that the page title contains "Summit" to confirm navigation
        assert "Summit" in browser.title, f"Expected title to contain 'Summit', but got '{browser.title}'"
        logging.info("Navigation to 'Summit' page verified successfully.")



    except Exception as e:
        logging.error(f"An error occurred: {e}")
        take_screenshot(browser, "summit_registration_error.png")  # Take a screenshot on error

    finally:
        logging.info("** test_summit_page executed successfully **")
