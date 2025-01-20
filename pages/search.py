from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from tests.conftest import browser


class DuckDuckGoSearchPage:

    SEARCH_INPUT = (By.ID, "searchbox_input")
    URL = "https://duckduckgo.com/"
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Search']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)


    def search(self, phrase):
         # * is the way in python to expand tuples into positional arguments that will be passed to the method
         # find_elemnt() take 2 arguments, locator type and locator. Tuple -> (type & locator)
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def search_then_click_btn(self, phrase):
        self.browser.find_element(*self.SEARCH_INPUT).send_keys(phrase)
        self.browser.find_element(*self.SEARCH_BUTTON).click()
