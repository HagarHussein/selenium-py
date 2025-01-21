from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from tests.conftest import browser
import time

class DuckDuckGoSearchPage:

    SEARCH_INPUT = (By.ID, "searchbox_input")
    URL = "https://duckduckgo.com/"
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Search']")

    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(self.browser)

    def load(self):
        self.browser.get(self.URL)


    def search(self, phrase):
         # * is the way in python to expand tuples into positional arguments that will be passed to the method
         # find_elemnt() take 2 arguments, locator type and locator. Tuple -> (type & locator)
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def search_then_click_btn(self, phrase):
        self.browser.find_element(*self.SEARCH_INPUT).send_keys(phrase)
        self.click_search_btn()

    def click_search_btn(self):
        self.browser.find_element(*self.SEARCH_BUTTON).click()


    def fill_search_textbox(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)

    def press_down_key_on_search_box(self):
        self.browser.find_element(*self.SEARCH_INPUT).click()
        self.actions.send_keys(Keys.ARROW_DOWN).perform()

    def search_input_value(self):
        return self.browser.find_element(*self.SEARCH_INPUT).get_attribute('value')

    def press_enter_key_on_search_box(self):
        self.browser.find_element(*self.SEARCH_INPUT).click()
        self.actions.send_keys(Keys.ENTER).perform()

