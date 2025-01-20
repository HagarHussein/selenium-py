import pytest

from pages.result import DuckDuckGoResultsPage
from pages.search import DuckDuckGoSearchPage

@pytest.mark.parametrize("phrase", ["Panda", "python", "polar bear"])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultsPage(browser)
    #PHRASE = "Panda"

    # Given the DuckduckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search results query pertain to "Panda"
    for title in result_page.results_link_titles():
        print(title)
        assert phrase.lower() in title.lower()

    # And the search result title contains "panda
    assert phrase in result_page.title()

    # TODO : remove it once test implementation is completed
    #raise Exception("Incomplete test")

@pytest.mark.ui
def test_duckduckgo_search_then_click_btn(browser):
    PHRASE = "Hardware tools"

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultsPage(browser)

    search_page.load()
    search_page.search_then_click_btn(PHRASE)

    assert PHRASE == result_page.search_input_value()
    assert PHRASE in result_page.title()
    for title in result_page.results_link_titles():
        assert PHRASE.lower() in title.lower()
