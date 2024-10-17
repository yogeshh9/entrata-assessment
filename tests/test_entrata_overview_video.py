from selenium.webdriver.common.by import By
import json
import requests
import logging
import pytest


@pytest.mark.overview_video
def test_EntrataOverviewVideo(browser):
    # Log the start of the test function execution
    logging.info("Executing test_EntrataOverviewVideo.")

    # Locate the script tag containing JSON data on the page
    script = browser.find_element(By.XPATH, "(//script[@type='application/json'])[1]")
    logging.info("Located the script tag containing JSON data.")

    # Retrieve the inner HTML content of the script tag
    scriptHTML = script.get_attribute("innerHTML")

    # Parse the JSON data from the script content
    data = json.loads(scriptHTML)
    logging.info("Parsed JSON data from the script.")

    # Extract the video URL from the parsed data
    video_url = data['items'][0]['url']
    logging.info(f"Extracted video URL: {video_url}")

    # Make a GET request to the video URL to verify it's accessible
    response = requests.get(video_url)
    logging.info(f"Requested video URL. Status code: {response.status_code}")

    # Assert that the response status code is 200 (OK), indicating the video is accessible
    assert response.status_code == 200, "Video URL is not accessible."
    logging.info("Video URL is accessible.")
    logging.info("** test_entrata_overview_video executed successfully **")