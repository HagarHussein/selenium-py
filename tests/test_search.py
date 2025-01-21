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

def test_search_result_redirection(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultsPage(browser)
    PHRASE = "Palestine"

    # GIVEN: the DuckduckGo home page is displayed
    search_page.load()

    # WHEN: the user searches for <phrase>
    search_page.search_then_click_btn(PHRASE)

    link = result_page.get_elem_link_by_index(0)
    # AND: user clicks on the first link in results page
    result_page.click_on_link_by_index(0)

    # THEN: the window is redirected to the new clicked url
    assert  result_page.get_current_window_url() == link


def test_more_results_links(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultsPage(browser)
    PHRASE = "Palestine"

    # GIVEN: the DuckduckGo home page is displayed
    search_page.load()

    # WHEN: the user searches for <phrase>
    search_page.search_then_click_btn(PHRASE)

    num_of_links_before = result_page.get_num_of_results_links()
    # AND: user click on "more results" link
    result_page.click_on_more_results()

    # THEN: the results links are expanded (number of links increases)
    num_of_links_after = result_page.get_num_of_results_links()
    assert num_of_links_after > num_of_links_before


def test_auto_complete_search_text(browser):
    search_page = DuckDuckGoSearchPage(browser)
    PHRASE = "Pale"

    # GIVEN: the DuckduckGo home page is displayed
    search_page.load()

    # WHEN: the user searches for <phrase initials>
    search_page.fill_search_textbox(PHRASE)

    # THEN: the suggested list all start with the same <phrase initials>
    for i in range(0,8):
        search_page.press_down_key_on_search_box()
        assert PHRASE not in search_page.search_input_value()


def test_auto_complete_search_results(browser):
    # GIVEN: the DuckduckGo home page is displayed
    # WHEN: the user searches for <phrase initials>
    # AND: user selects first suggestion
    # THEN: the search results links contains the  <selected phrase suggestion>
    # AND: the search result title contains <phrase>
    # AND: the search result query is <phrase>
    raise Exception("Not Implemented Test")

def test_search_from_results_page(browser):
    # GIVEN: the DuckduckGo home page is displayed
    # WHEN: the user searches for <phrase>
    # AND: user changes the search in the results page to <phrase>
    # THEN: the search results are changed into the new <phrase> (all links)
    # AND: the search result title contains <phrase>
    # AND: the search result query is <phrase>
    raise Exception("Not Implemented Test")

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

