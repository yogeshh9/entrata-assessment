import logging
import pytest

@pytest.mark.homepage_title
def test_HomepageTitle(browser):
    # Log the start of the test function execution
    logging.info("** Executing test_HomepageTitle **")

    # Assert that the title of the homepage is as expected
    expected_title = 'Property Management Software | Entrata'
    actual_title = browser.title

    logging.info("Expected title: %s", expected_title)
    logging.info("Actual title: %s", actual_title)

    assert actual_title == expected_title, f"Expected title '{expected_title}' but got '{actual_title}'."
    logging.info("Homepage title verified successfully.")


    logging.info("** test_homepage_title executed successfully **")
