import pytest

from pages.result import DuckDuckGoResultsPage
from pages.search import DuckDuckGoSearchPage

def test_search_from_results_page(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultsPage(browser)
    phrase = "Palestine"

    # GIVEN: the DuckduckGo home page is displayed
    search_page.load()

    # WHEN: the user searches for <phrase>
    search_page.search_then_click_btn(phrase)

    # AND: user changes the search in the results page to <phrase>
    phrase = "lion"
    result_page.clear_search_box()
    result_page.search_from_results(phrase)


    # AND: the search result title contains <phrase>
    assert phrase in result_page.title()

    # AND: the search result query is <phrase>
    assert phrase == result_page.search_input_value()

    # THEN: the search results are changed into the new <phrase> (all links)
    for title in result_page.results_link_titles():
        print(title)
        assert phrase.lower() in title.lower()


def test_search_images(browser):
    # GIVEN: the DuckduckGo home page is displayed
    # WHEN: the user searches for <phrase>
    # AND: user select images results
    # THEN: the search results are changed into images with titles containing <phrase>
    # AND: image resolution label appears
    raise Exception("Not Implemented Test")

def test_search_videos(browser):
    # GIVEN: the DuckduckGo home page is displayed
    # WHEN: the user searches for <phrase>
    # AND: user select videos results
    # THEN: the search results are changed into videos with video names containing <phrase>
    # AND: video source img and label appears
    raise Exception("Not Implemented Test")

def test_search_news(browser):
    # GIVEN: the DuckduckGo home page is displayed
    # WHEN: the user searches for <phrase>
    # AND: user select news results
    # THEN: the search results are changed into news
    raise Exception("Not Implemented Test")