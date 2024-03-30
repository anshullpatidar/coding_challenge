from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.common_page_elements import CommonPageElements
from src.helper import Helper


class HomePage(CommonPageElements, Helper):
    LOCATOR_FILE = "home_page.yaml"

    def __init__(self, driver):
        super().__init__(driver)
        Helper().__init__()
        self.page_locators = self.get_locators(self.LOCATOR_FILE)

    def check_search_stock(self):
        ele = self.get_page_element(self.page_locators["search-box"])
        return ele if ele else False

    def enter_stock_to_search(self, text):
        self.enter_text_to_element(self.page_locators["search-box"], text, is_enter=True)
        WebDriverWait(self.driver, 10).until(EC.title_contains(text))
        return True

    def navigate_to_most_active_page(self, page_title):
        self.click_element(self.page_locators["most-active"])
        WebDriverWait(self.driver, 10).until(EC.title_is(page_title))

    def navigate_to_market(self, market):
        market = market.lower()
        self.click_element(self.page_locators["markets-" + market + ""])
        WebDriverWait(self.driver, 10).until(EC.title_contains("Finance"))

    def get_dow_jones_index_text(self):
        return self.get_element_text(self.page_locators["index-dow-jones"])

    def get_dax_index_text(self):
        return self.get_element_text(self.page_locators["index-dax"])

    def get_nifty_index_text(self):
        return self.get_element_text(self.page_locators["index-nifty-50"])

    def login(self, email, password):
        self.click_element(self.page_locators["sign-in"])
        self.enter_text_to_element(self.page_locators["email"], email, is_enter=False)
        self.click_element(self.page_locators["next_button"])
        self.enter_text_to_element(self.page_locators["password"], password, is_enter=False)
        self.click_element(self.page_locators["next_button"])

    def get_wrong_password_text(self):
        return self.get_element_text(self.page_locators["wrong_password_text"])

    def navigate_local_market_financial_news(self):
        self.click_element(self.page_locators["local-market"])

    def navigate_top_stories_financial_news(self):
        self.click_element(self.page_locators["top-stories"])

    def navigate_world_markets_financial_news(self):
        self.click_element(self.page_locators["world-markets"])

    def get_most_followed_stocks_list_count(self):
        return len(self.get_page_element_list(self.page_locators["most-followed-list"]))

    def get_discover_more_list_count(self):
        return len(self.get_page_element_list(self.page_locators["discover-more"]))
