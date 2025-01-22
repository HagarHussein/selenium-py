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
        assert phrase.lower() in title.lower()


def test_search_images(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultsPage(browser)
    phrase = "Palestine"

    # GIVEN: the DuckduckGo home page is displayed
    search_page.load()

    # WHEN: the user searches for <phrase>
    search_page.search_then_click_btn(phrase)

    # AND: user select images results
    result_page.click_on_images_link()

    # THEN: the search results shows images
    assert result_page.check_img_results_existed() == True

    # AND : the search results links list is not empty
    assert len(result_page.get_img_results_links()) != 0


def test_search_videos(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultsPage(browser)
    phrase = "Palestine"

    # GIVEN: the DuckduckGo home page is displayed
    search_page.load()

    # WHEN: the user searches for <phrase>
    search_page.search_then_click_btn(phrase)

    # AND: user select videos results
    result_page.click_on_videos_link()

    # THEN: video source img and label appears
    assert result_page.check_video_source_results_existed() == True
    assert result_page.check_video_source_logo_existed() == True
