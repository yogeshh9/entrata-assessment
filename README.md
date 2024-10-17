# Entrata Assessment

This repository contains Selenium tests designed to explore and validate the functionality of [Entrata](https://www.entrata.com).

## Overview

The tests cover various aspects of the Entrata website, including:
- Homepage title verification
- Demo form submission
- Checking if the Entrata overview video is accessible
- Navigation through product sections
- Verification of the summit page
- and more

## Requirements

- Python 3.x
- pip
- ChromeDriver (ensure it matches your Chrome version)
- pytest
- Selenium
- requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yogeshh9/entrata-selenium-tests.git
   cd entrata-selenium-tests
   
2. Install the required packages:
   ```bash
   pip install -r requirements.txt


## Running the Tests

- To run the entire test suite, use the following command:
  ```
  pytest

- To run specific tests based on markers, use:
  ```
  pytest -m <marker name>

## The project is organized as follows:

tests/: Contains all test cases.
logss/: Contains all test logs.
reports/: Contains all execution reports.
screenshots/: Contains all nescessary test case screenshots .
utils/: Contains utility functions for waiting for elements and other common actions.
pytest.ini: Configuration file for pytest, including test markers and report options.


