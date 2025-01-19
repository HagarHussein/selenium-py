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