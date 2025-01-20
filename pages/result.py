from selenium.webdriver.common.by import By
from tests.conftest import browser


class DuckDuckGoResultsPage:
    RESULTS_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    SEARCH_INPUT = (By.ID, "search_form_input")

    def __init__(self, browser):
        self.browser = browser

    def results_link_titles(self):
        links = self.browser.find_elements(*self.RESULTS_LINKS)
        return [link.text for link in links]

    def search_input_value(self):
        return self.browser.find_element(*self.SEARCH_INPUT).get_attribute('value')

    def title(self):
        return self.browser.title

    def click_on_link_by_index(self, index):
        self.browser.find_elements(*self.RESULTS_LINKS)[index].click()

    def get_elem_link_by_index(self, index):
        return self.get_href_link(self.browser.find_elements(*self.RESULTS_LINKS)[index])

    def get_href_link(self, elem):
        return elem.get_attribute("href")

    def get_current_window_url(self):
        return self.browser.current_url

