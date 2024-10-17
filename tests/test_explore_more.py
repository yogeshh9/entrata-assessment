from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.expected_conditions as EC
from utils.webdriver_utils import scroll_to_element, wait_for_element
import pytest
import logging

@pytest.mark.explore_more
def test_explore_more(browser):
    # Log the start of the test function execution
    logging.info("Executing test_explore_more.")

    action = ActionChains(browser)

    # Locate the 'Explore More' button
    explore_more_btn = browser.find_element(By.XPATH, "//div[text()='Explore More']")
    logging.info("Located 'Explore More' button.")

    # Scroll to the button
    scroll_to_element(browser, explore_more_btn)

    # Wait until the button is clickable and click it
    wait_for_element(browser, By.XPATH, "//div[text()='Explore More']", EC.element_to_be_clickable)
    action.move_to_element(explore_more_btn).click().perform()
    logging.info("Clicked 'Explore More' button.")

    # Switch to the new tab
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    logging.info("Switched to new tab.")

    # Log the title and URL of the new tab
    logging.info("New Tab Title: %s", browser.title)
    logging.info("New Tab URL: %s", browser.current_url)

    # Assert the new tab title and URL
    assert browser.title == "Basecamp 2025 | Entrata"
    assert browser.current_url == "https://basecamp.entrata.com/"
    logging.info("Verified new tab title and URL.")

    # Switch back to the old tab
    browser.switch_to.window(windows[0])
    logging.info("Switched back to old tab.")

    # Wait for the URL to contain the expected value
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_contains("https://www.entrata.com/a"))

    # Log the title and URL of the old tab
    logging.info("Old Tab Title: %s", browser.title)
    logging.info("Old Tab URL: %s", browser.current_url)

    # Assert the old tab title and URL
    assert browser.title == "Property Management Software | Entrata"
    assert browser.current_url == "https://www.entrata.com/a"
    logging.info("Verified old tab title and URL.")

    logging.info("** test_explore_more executed successfully **")

