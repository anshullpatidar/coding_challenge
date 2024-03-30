from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.common_page_elements import CommonPageElements
from src.helper import Helper


class StockDetailPage(CommonPageElements, Helper):
    LOCATOR_FILE = "stock_details_page.yaml"

    def __init__(self, driver):
        super().__init__(driver)
        Helper().__init__()
        self.page_locators = self.get_locators(self.LOCATOR_FILE)

    def get_stock_price(self):
        return self.get_element_text(self.page_locators["stock-price"])
