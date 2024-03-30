# Google Finance Automation

This project is about automating major functionalities of Google Finance using Pytest and Selenium.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.12
- Firefox browser and geckodriver installation is done through run_pytest.sh script.
- If you need to run test on chrome browser, you need to install the chrome browser and the chromedriver.
  
### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Download the zip and extract
2. Navigate to the project directory coding_challenge 
    $ cd coding_challenge

## Running the tests

1. Give permission to the shell script:
    $ chmod +x run_pytest.sh
2. Execute the following command to run the tests in headless mode on firefox browser(default):
    $ ./run_pytest.sh
3. Post execution, the test report will be generated in the "reports" directory and 
   screenshots will be saved in the "reports/screenshots" directory.
4. The test report will be in the html format and can be viewed in the browser.
   Html report path - coding_challenge/reports/html-report.html
5. To execute the tests on the chrome browser, you can pass the browser

Note: 
1. The above command will run the tests in headless mode on firefox browser by default.
2. The script also handles the installation of the required packages using pip, so you don't need to install them manually.
3. The script will also create a virtual environment for the project and install the required packages in it.
4. The script will also install the geckodriver for the firefox browser. 
5. If you want to see the browser in action, you can remove the `--headless` option from the `run_pytest.sh`file at line 72. 
            pytest $TEST_DIR --headless False

## Authors

- Anshul Patidar