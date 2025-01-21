from selenium.webdriver.common.by import By
from tests.conftest import browser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoResultsPage:
    RESULTS_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    SEARCH_INPUT = (By.ID, "search_form_input")
    MORE_RESULTS = (By.ID, "more-results")
    PAGE_2_RESULTS = (By.CSS_SELECTOR, "div[aria-label='Page 2']")

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

    def scroll_to_element_action(self, elem):
        actions = ActionChains(self.browser)
        actions.move_to_element(elem).perform()

    def scroll_to_element_js(self, elem):
        self.browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", elem)

    def click_on_more_results(self):
        elem = self.browser.find_element(*self.MORE_RESULTS)
        self.scroll_to_element_js(elem)
        elem.click()

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(self.PAGE_2_RESULTS))


    def get_num_of_results_links(self):
        return len(self.browser.find_elements(*self.RESULTS_LINKS))

