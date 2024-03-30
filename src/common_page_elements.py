from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CommonPageElements:

    def __init__(self, driver):
        self.driver = driver

    def get_page_element(self, locator):
        """
        This function will return the element based on the locator
        :param driver:
        :param locator:
        :return:
        """

        find_by = None
        if locator["type"] == "id":
            find_by = By.ID
        elif locator["type"] == "xpath":
            find_by = By.XPATH
        elif locator["type"] == "css":
            find_by = By.CSS_SELECTOR
        elif locator["type"] == "name":
            find_by = By.NAME
        elif locator["type"] == "class":
            find_by = By.CLASS_NAME
        elif locator["type"] == "link_text":
            find_by = By.LINK_TEXT
        elif locator["type"] == "partial_link_text":
            find_by = By.PARTIAL_LINK_TEXT
        elif locator["type"] == "tag_name":
            find_by = By.TAG_NAME

        if find_by:
            return self.driver.find_element(find_by, locator["value"])
        else:
            print("Invalid locator type {} for locator {}".format(locator['type'], locator['value']))
            return None

    def click_element(self, locator):
        try:
            ele = self.get_page_element(locator)
            return ele.click()
        except Exception as e:
            print("Exception occurred: {}".format(e))

    def get_element_text(self, locator):
        try:
            ele = self.get_page_element(locator)
            return ele.text
        except Exception as e:
            print("Exception occurred: {}".format(e))

    def enter_text_to_element(self, locator, text, is_enter=False):
        try:
            ele = self.get_page_element(locator)
            ele.send_keys(text)
            if is_enter:
                ele.send_keys(Keys.ENTER)
        except Exception as e:
            print("Exception occurred: {}".format(e))

    def get_page_element_list(self, locator):
        return self.driver.find_elements(locator["type"], locator["value"])
