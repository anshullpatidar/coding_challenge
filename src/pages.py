
from src.home_page import HomePage
from src.market_trends import MarketTrendsPage
from src.stock_details_page import StockDetailPage


class Pages:

    def __init__(self, driver):
        self.home = HomePage(driver)
        self.market_page = MarketTrendsPage(driver)
        self.stock_details_page = StockDetailPage(driver)


