import logging
import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By


# Configure logging and reporting
def pytest_configure(config):
    log_filename = f"./logs/test_log{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        filename= log_filename,
        format= '%(asctime)s %(levelname)s %(message)s'
    )

    report = f"test_report{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
    config.option.htmlpath = os.path.join("reports", report)


# Creating fixture to set up a Selenium WebDriver instance for all tests
@pytest.fixture
def browser():
    # Initializing the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigating to the Entrata homepage
    logging.info("Navigating to the Entrata homepage.")
    driver.get("https://www.entrata.com/a")

    # Initializing explicit wait with a 10-second timeout
    wait = WebDriverWait(driver, 10)

    try:
        # Wait for the cookie consent button to be clickable
        cookie_consent = wait.until(
            EC.element_to_be_clickable((By.ID, "cookie-accept"))
        )
        # Click the cookie consent button if found
        cookie_consent.click()
        logging.info("Cookie consent accepted.")
    except Exception as e:
        # Log an error if the cookie consent button is not found
        logging.warning("Cookie consent button not found: %s", e)

    # Maximizing the browser window for better visibility during tests
    driver.maximize_window()
    logging.info("Browser window maximized.")

    # Set an implicit wait for other elements
    driver.implicitly_wait(10)

    try:
        # Wait for the ad close button to be clickable
        ad = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']"))
        )
        # Click the ad close button if found
        ad.click()
        logging.info("Ad closed.")
    except Exception as e:
        # Log an error if the ad close button is not found
        logging.warning("Ad close button not found: %s", e)

    # Yield the driver for use in tests
    yield driver

    # Teardown the driver to close all associated windows after tests are done
    logging.info("Closing the browser.")
    driver.quit()