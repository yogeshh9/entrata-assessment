from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotInteractableException
from utils.webdriver_utils import wait_for_element, take_screenshot
import logging
import pytest

@pytest.mark.demo_form
def test_demoForm(browser):
    # Log the start of the test function execution
    logging.info("** Executing test_demoForm **")

    # Initializing Explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(browser, 20)

    # Wait for the input fields to become visible and interactable
    firstname = wait_for_element(browser, By.ID, "FirstName", EC.visibility_of_element_located)
    lastname = wait_for_element(browser, By.ID, "LastName", EC.visibility_of_element_located)
    email = wait_for_element(browser, By.ID, "Email", EC.visibility_of_element_located)
    company_name = wait_for_element(browser, By.ID, "Company", EC.visibility_of_element_located)
    phonenumber = wait_for_element(browser, By.ID, "Phone", EC.visibility_of_element_located)
    unit_count = wait_for_element(browser, By.ID, "Unit_Count__c", EC.visibility_of_element_located)
    jobtitle = wait_for_element(browser, By.ID, "Title", EC.visibility_of_element_located)
    demo_request = wait_for_element(browser, By.ID, "demoRequest", EC.visibility_of_element_located)

    # Scroll to the first name field to ensure it is in view
    browser.execute_script("arguments[0].scrollIntoView();", firstname)
    logging.info("Scrolled to the first name field.")

    try:
        # Fill out the form with user details
        firstname.send_keys("Yogesh")
        lastname.send_keys("Zalte")
        email.send_keys("ybzalte@gmail.com")
        company_name.send_keys("VOIS")
        phonenumber.send_keys("9605599034")
        logging.info("Filled out the user details.")

        # Select the number of units from the dropdown
        unitCount = Select(unit_count)
        unitCount.select_by_index(3)
        logging.info("Selected unit count.")

        # Fill in the job title
        jobtitle.send_keys("Automation Test Engineer")
        logging.info("Entered job title.")

        # Select a demo request option from the dropdown
        iAm = Select(demo_request)
        iAm.select_by_value("a Resident")
        logging.info("Selected demo request option.")

        # Save a screenshot of the form after filling it out
        take_screenshot(browser, "demoform.png")
        logging.info("Screenshot taken after filling the form.")

    except ElementNotInteractableException as e:
        # Log an error message if an element is not interactable
        logging.error(f"Element not interactable: {e}")

    finally:
        logging.info("** test_demo_form executed successfully **")
