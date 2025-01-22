from selenium.webdriver.common.by import By
from tests.conftest import browser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class DuckDuckGoResultsPage:


    RESULTS_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    SEARCH_INPUT = (By.ID, "search_form_input")
    MORE_RESULTS = (By.ID, "more-results")
    PAGE_2_RESULTS = (By.CSS_SELECTOR, "div[aria-label='Page 2']")
    SEARCHES_RELATED_TO_TEXT = (By.CSS_SELECTOR, "p.related-searches__title-long")
    IMAGES_LINK = (By.XPATH, "//a[text()='Images']")
    RESULTS_IMGS = (By.CSS_SELECTOR, 'img.tile--img__img')
    VIDEOS_LINK = (By.XPATH, "//a[text()='Videos']")
    VIDEO_SOURCE = (By.CSS_SELECTOR, "span.video-source")
    VIDEO_SOURCE_LOGO = (By.CSS_SELECTOR, 'img.tile__favicon')
    NEWS_LINK = (By.XPATH, "//a[text()='News']")

    def __init__(self, browser):
        self.browser = browser
        self.WAIT = WebDriverWait(self.browser, 20)

    def results_link_titles(self):
        links = self.browser.find_elements(*self.RESULTS_LINKS)
        return [link.text for link in links]

    def search_input_value(self):
        return self.browser.find_element(*self.SEARCH_INPUT).get_attribute('value')

    def title(self):
        # using this wait condition to make sure the document is ready before returning its title
        # to make sure it will become ready for any preceding actions in the tests
        self.WAIT.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete")
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

        self.WAIT.until(EC.presence_of_element_located(self.PAGE_2_RESULTS))


    def get_num_of_results_links(self):
        return len(self.browser.find_elements(*self.RESULTS_LINKS))

    def search_from_results(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def clear_search_box(self):
        self.browser.find_element(*self.SEARCH_INPUT).clear()

    def click_on_images_link(self):
        self.WAIT.until(EC.presence_of_element_located(self.IMAGES_LINK))
        self.browser.find_element(*self.IMAGES_LINK).click()

    def check_img_results_existed(self):
        try:
            return self.browser.find_element(*self.RESULTS_IMGS).is_displayed()
        except NoSuchElementException:
            return False

    def click_on_videos_link(self):
        self.WAIT.until(EC.presence_of_element_located(self.VIDEOS_LINK))
        self.browser.find_element(*self.VIDEOS_LINK).click()

    def check_video_source_results_existed(self):
        try:
            return self.browser.find_element(*self.VIDEO_SOURCE).is_displayed()
        except NoSuchElementException:
            return False

    def check_video_source_logo_existed(self):
        try:
            return self.browser.find_element(*self.VIDEO_SOURCE_LOGO).is_displayed()
        except NoSuchElementException:
            return False

    def click_on_news_link(self):
        self.WAIT.until(EC.presence_of_element_located(self.NEWS_LINK))
        self.browser.find_element(*self.NEWS_LINK).click()
