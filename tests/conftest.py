import os
import pytest
from selenium import webdriver
from src.pages import Pages
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

SCREENSHOT_PATH = os.path.join(os.path.dirname(__file__), "../screenshots")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Type in browser type")
    parser.addoption(
        "--headless", action="store_true", default=True, help="Run tests in headless mode."
    )


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser").lower()


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope='session')
def get_base_url():
    return os.environ.get("BASE_URL", "https://finance.google.com")


@pytest.fixture(scope="function")
def browser(request, browser_type, get_base_url, headless):
    request.node.name = request.node.name.replace(" ", "_")
    # Initialize ChromeDriver
    if browser_type == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    # Initialize FirefoxDriver
    elif browser_type == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    driver.get(get_base_url)
    driver.maximize_window()

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


@pytest.fixture(scope="function")
def get_pages_object(browser):
    pages_obj = Pages(browser)
    return pages_obj
