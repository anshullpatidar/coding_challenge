from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.common_page_elements import CommonPageElements
from src.helper import Helper


class MarketTrendsPage(CommonPageElements, Helper):
    LOCATOR_FILE = "market_trends_page.yaml"

    def __init__(self, driver):
        super().__init__(driver)
        Helper().__init__()
        self.page_locators = self.get_locators(self.LOCATOR_FILE)

    def get_header_text(self):
        return self.get_element_text(self.page_locators["explore-market-trends"])


