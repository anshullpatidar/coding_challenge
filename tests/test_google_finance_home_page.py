import time

import pytest


class TestGoogleFinance:

    @pytest.mark.smoke
    def test_search_stock(self, browser, get_pages_object):
        get_pages_object.home.check_search_stock()
        get_pages_object.home.enter_stock_to_search("Keysight Technologies Inc")
        assert "Keysight Technologies Inc" in browser.title, "Title is not matching"

    @pytest.mark.smoke
    def test_compare_markets_navigation(self, browser, get_pages_object):
        get_pages_object.home.navigate_to_market("US")
        assert "Dow Jones" in get_pages_object.home.get_dow_jones_index_text()
        get_pages_object.home.navigate_to_market("Europe")
        assert "DAX" in get_pages_object.home.get_dax_index_text()
        get_pages_object.home.navigate_to_market("India")
        assert "NIFTY 50" in get_pages_object.home.get_nifty_index_text()
        assert "Google Finance - Stock Market Prices" in browser.title, "Title is not matching"

    def test_market_trends_navigation(self, browser, get_pages_object):
        get_pages_object.home.navigate_to_most_active_page(page_title="Most Active Stocks - Google Finance")
        assert "Most Active Stocks - Google Finance" in browser.title, "Title is not matching"
        assert "Explore market trends\nShare" in get_pages_object.market_page.get_header_text()

    def test_new_watchlist(self, browser, get_pages_object):
        # To test / automate this functionality we will need valid credentials to sign in.
        # Google has restricted to automate sign in
        assert "Google Finance - Stock Market Prices" in browser.title, "Title is not matching"

    def test_new_portfolio(self, browser, get_pages_object):
        # To test / automate this functionality we will need valid credentials to sign in.
        # Google has restricted to automate sign in
        assert "Google Finance - Stock Market Prices" in browser.title, "Title is not matching"

    @pytest.mark.smoke
    def test_most_followed_on_google(self, browser, get_pages_object):
        assert get_pages_object.home.get_most_followed_stocks_list_count() > 0, "No items in most followed stocks list"

    def test_financial_news_navigation(self, browser, get_pages_object):
        get_pages_object.home.navigate_local_market_financial_news()
        get_pages_object.home.navigate_top_stories_financial_news()
        get_pages_object.home.navigate_world_markets_financial_news()
        assert "Google Finance - Stock Market Prices" in browser.title, "Page should not change"

    @pytest.mark.smoke
    def test_stock_price_visible(self, browser, get_pages_object):
        get_pages_object.home.check_search_stock()
        get_pages_object.home.enter_stock_to_search("Keysight Technologies Inc")
        assert get_pages_object.stock_details_page.get_stock_price() != "", "The value should not be blank."

    def test_discover_more_list(self, browser, get_pages_object):
        assert get_pages_object.home.get_discover_more_list_count() > 0, "No stocks in most followed list"

    @pytest.mark.skip
    def test_invalid_login(self, browser, get_pages_object):
        # To test / automate this functionality we will need valid credentials to sign in.
        # Google has restricted to automate sign in.
        get_pages_object.home.login("abc@test.com", "wrong@pwd")
        assert ("Wrong password. Try again or click ‘Forgot password’ to reset it."
                in get_pages_object.home.get_wrong_password_text())
