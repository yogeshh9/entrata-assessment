from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logging

def wait_for_element(browser, by, value, condition, timeout=20):
    return WebDriverWait(browser, timeout).until(condition((by, value)))

def take_screenshot(browser, filename):
    browser.save_screenshot(f"./screenshots/{filename}")

def hover_over_elements(browser, elements):

    #  browser: The WebDriver instance.
    #  elements: A list of tuples containing the WebElement and descriptive name for logging.

    action = ActionChains(browser)

    for element, name in elements:
        action.move_to_element(element).perform()
        logging.info(f"Hovered over '{name}'.")


def scroll_to_element(browser, element):
    """Scroll to the specified element."""
    element_position = element.location['y']
    viewport_height = browser.execute_script("return window.innerHeight")
    scroll_position = element_position - (viewport_height / 2)
    browser.execute_script("window.scrollTo(0, arguments[0]);", scroll_position)
    logging.info(f"Scrolled to position: {scroll_position}.")